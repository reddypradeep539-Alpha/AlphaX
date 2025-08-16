report_data = []
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from imdb import IMDb
import requests
import datetime


# Email function
def send_email(to_email, subject, body):
    try:
        # Your email details
        sender_email = "varunbengaluru123@gmail.com"  # Replace with your email
        sender_password = "ztyk sfcl ddlh pfap"  # Replace with your email password or app password (if 2FA enabled)
        
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establish connection with Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        st.success(f"Email sent successfully to {to_email}")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# Set page title
st.set_page_config(page_title="Piracy Hunter X", layout="centered")

st.title("🎬 Piracy Hunter X")
st.subheader("An AI-Powered Anti-Piracy Tool")

# Your SerpAPI Key
SERPAPI_KEY = "75d37408b10d8117205fa71c84a7afdfe5943fce8efc86f33dd5f4fb43970e87"

# Function to search links using SerpAPI
def search_links(query, num_results=10):
    search_url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": num_results,
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    links = [result.get("link") for result in data.get("organic_results", [])]
    return links

# Piracy Link Detector (AI Filter) - Simple Keyword Filtering
def piracy_link_detector(link):
    piracy_keywords = [
        "watch free","t.me","telegram", "youtube","Download", "download" "leaked print", "480p", "HD download", "full movie free",
        "free download", "watch online", "torrent", "download movie", "free hd movie",
        "watch movie online free", "torrent download", "stream free", "leak movie"
    ]
    
    link_lower = link.lower()
    for keyword in piracy_keywords:
        if keyword in link_lower:
            return "Pirated"
    return "Safe ✅ "

# Get movies from user
movie_names_input = st.text_area("Enter Movie Names (comma or newline separated):")
movie_names = [name.strip() for name in movie_names_input.replace('\n', ',').split(',') if name.strip()]

# Step 1: Verify Movies
if movie_names:
    if st.button("Verify Movies"):
        ia = IMDb()
        for movie_name in movie_names:
            results = ia.search_movie(movie_name)
            if results:
                movie = results[0]
                title = movie['title']
                st.success(f"✅ '{movie_name}' found as '{title} '")
            else:
                st.error(f"❌ Movie '{movie_name}' not found.")

# Step 2: Start Piracy Scan
if st.button("Start Piracy Scan for All Movies"):
    ia = IMDb()
    for movie_name in movie_names:
        results = ia.search_movie(movie_name)
        if results:
            movie = results[0]
            title = movie['title']
            year = movie.get('year', 'Unknown')
            full_title = f"{title} ({year})"

            query1 = f"{full_title} download site:telegram.me OR site:t.me"
            query2 = f"{full_title} full movie download"
            links = list(set(search_links(query1, 10) + search_links(query2, 10)))

            # Layout: Show in 4 columns
            col1, col2, col3, col4= st.columns(4)

            with col1:
                st.markdown(f"### 🎥 {full_title}")
                st.write(f"🔎 Links Found: {len(links)}")
                st.write(f"🕒 Scanned at: {datetime.datetime.now().strftime('%I:%M:%S %p')}")

            with col2:
                st.markdown("### 🌐 Links")
                if links:
                    for link in links:
                        st.write(link)
                else:
                    st.write("No links found.")

            with col3:
                st.markdown("### 🚨 Actions")
                st.write("✅ Links Processed")
                st.write("🔒 Links Reported")
                st.write("❌ Links Deleted: 0")
                st.write("📝 Links Reported: 0")

            # Automatically classify the links as Pirated or Safe/Unknown
            for link in links:
                result = piracy_link_detector(link)
                report_data.append({
                     "movie": full_title,
                      "link": link,
                      "status": result
                    })
                st.write(f"Link: {link} is classified as: {result}")

                # Send takedown email ONLY for pirated (unsafe) links
                if result == "Pirated":
                    email_subject = f"Takedown Request for {full_title}"
                    email_body = f"Dear Sir/Madam,\n\nWe request you to remove the following piracy link for the movie '{full_title}':\n\n{link}\n\nThis content violates copyright law and is being distributed without authorization. We request prompt action to take down this content.\n\nThank you."

                    # Send email (you can modify the to_email as needed)
                    send_email("recipient_email@example.com", email_subject, email_body)

# UI for Movie and Links Overview
st.markdown("🚨 Takedown Email Automation")
st.markdown("""This feature automatically sends takedown emails for piracy hosting websites/channels detected in your piracy scan.
You no longer need to manually enter piracy links – they are detected based on movie names.""")



