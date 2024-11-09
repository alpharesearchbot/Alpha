import re

# Define regex patterns to identify unwanted lines
patterns = [
    r"^Content-Type:",              
    r"^Content-Transfer-Encoding:",  
    r"^MIME-Version:",               
    r"^Date:",                       
    r"^From:",                       
    r"^To:",                         
    r"^To:",                         
    r"^Subject:",                    
    r"^In-Reply-To:",                
    r"^References:",                 
    r"^Message-ID:",                 
    r"^User-Agent:",                 
    r"^X-Sender:",                   
    r"\b<.*?@.*?>",                  
    r"\b=\?UTF-\d+\?Q\?.*?\?=",      
    r"^Roundcube Webmail\/.*",        
    r"^\d{4}-\d{2}-\d{2}",          
    r"^\d{1,2}:\d{2}",               
    r"^[A-Za-z]+,",                  
    r"^--$",                         
]


combined_pattern = re.compile("|".join(patterns))

content_lines = []

with open("testMail.eml", 'r', encoding="utf-8") as eml_file:
    for line in eml_file:
       
        line = line.strip()

       
        if not combined_pattern.search(line):
            content_lines.append(line + '\n')  


output_path = "cleaned_output.txt"
with open(output_path, 'w', encoding='utf-8') as result_file:
    result_file.writelines(content_lines)

print(f"Cleaned content saved to {output_path}")
