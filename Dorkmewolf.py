from googlesearch import search
import urllib.parse

banner = """
               ________________
              ____/ (  (    )   )  \___
             /( (  (  )   _    ))  )   )\\
           ((     (   )(    )  )   (   )  )
         ((/  ( _(   )   (   _) ) (  () )  )
        ( (  ( (_)   ((    (   )  .((_ ) .  )_
       ( (  )    (      (  )    )   ) . ) (   )
      (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
      ( (  (   ) (  )   (  ))     ) _)(   )  )  )
     ( (  ( \\ ) (    (_  ( ) ( )  )   ) )  )) ( )
      (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
     ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
      ((  (   )(    (     _    )   _) _(_ (  (_ )
       (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
       ((__)        \\\\||lll|l||///          \_))
                (   /(/ (  )  ) )\\   )
               (    ( ( ( | | ) ) )\\   )
                (   /(| / ( )) ) ) )) )
              (     ( ((((_(|)_)))))     )
               (      ||\\(|(|)|/||     )
             (        |(||(||)||||        )
               (     //|/l|||)|\\\\ \\     )
             (/ / //  /|//||||\\\\  \\ \\  \\ _)
-------------------------------------------------------------------------------
"""
print(banner)

def extract_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

def google_dork_search(query, num_results=100):
    results = search(query, num_results=num_results)
    return results

def save_domains_to_file(domains, filename='domains.txt'):
    with open(filename, 'w') as file:
        for domain in domains:
            file.write(domain + '\n')

if __name__ == "__main__":
    # Define your Google Dork query here
    dork_query = 'site:go.ke admin'

    # Number of search results to fetch
    num_results = 100

    # Perform the Google Dork search
    search_results = google_dork_search(dork_query, num_results)

    # Extract domains from URLs and remove duplicates
    unique_domains = set(extract_domain(url) for url in search_results)

    # Display the results
    print("Unique domains found:")
    for domain in unique_domains:
        print(domain)

    # Save the unique domains to a file
    save_domains_to_file(unique_domains)
    print(f"Unique domains saved to domains.txt")
