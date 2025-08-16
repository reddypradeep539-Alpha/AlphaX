# An - Anti Piracy Tool  [ Ai - CyberSecurity ]

Project Title: Piracy Hunter X – Smart AI Tool to Detect Piracy Links and Report, infect them.

Project Goal:
To automatically detect and infect or report pirated film download links from platforms like Telegram and websites, using film titles of recently released movies, and then generate an automatic report showing all the actions taken.


 How It Works – Step-by-Step:

✅ 1. Film Title Collector
     Automatically fetch the names of newly released movies (e.g., from IMDb,BookMyShow, or a simple JSON list).
     Example: “Pooja 2025”, “Action Hero 2”, “Vikram Returns”
    
2. Smart Link Searcher
     For each movie title:
        o Search the web (Google, Bing) for phrases like:
     "<movie name> full movie download"
     "<movie name> Telegram link"
        Scrape Telegram channel preview data (optional APIs or manually throughweb scraping or bot)
        Collect all suspicious links
    
3. Piracy Link Detector (AI filter)

   Use simple machine learning or keyword filtering:
    o If the link contains known piracy terms like watch free, leaked print, 480p, HD download, it’s marked as pirated.
    o Otherwise, marked as safe or unknown.
    
4. Action Engine – Send Warn mail to the aunathorised owner ] 
   Attempt to:
    o Delete links using Telegram Bot API (if it’s your bot) or reporting system.
    o Auto-generate takedown emails for piracy-hosting websites.
    o Mark status: Deleted / Reported / Infected 

 5. Auto Report Generator
     After scanning:
      o Show a report like:
     Movie: KGF
      Links Found: 25
     ✅ Deleted: 15
     Reported: 10
     Time: 04/25/2025
     Display in a dashboard or download as PDF.


Quick summary

 Uses Google search + scraping to find suspicious links.
 Uses a simple rule-based piracy detector.
 Display links and actions in a web page.
 Generate report. 
