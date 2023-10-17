#socket library
import socket
#command line parameter parsing
import argparse
from urllib.parse import urlparse,ParseResult
import re
import os

#Function to fetch image 
def download_Html(url):
    try:
        #Parse the URL to txtract the path 
        u = urlparse(url)
        host = u.netloc
        path = u.path if u.path else '/'

        #creating socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket Created")

        #server's hostname or IP address
        HOST = "www.google.com"  
        #port number used by google
        PORT = 80        
        
        #connecting to the Remote Server
        s.connect((HOST, PORT))
        print("successfully connected")
            
        #send HTTP GET request (to fetch the data from the server)
        request = f"GET / HTTP/1.0\r\nHost:{HOST}\r\n\r\n"
        s.send(request.encode('UTF-8'))
        print("successfully sent HTTP request")
        
        #Receive the response    
        response = b""
        while True:    
                data = s.recv(1024)
                if not data:
                    break
                response += data


        #Close the socket
        s.close()

        # Split the response into headers and content
        response = response.split(b'\r\n\r\n', 1)
        headers = response[0]
        content = response[1] if len(response) > 1 else b""

        return content.decode('utf-8')
        #return response
    except Exception as e:
            print(f"Failed. Error: {e}")
            return None
       
#function to extract <img> tags from HTML content  
def IMG_tags(html_content):
    try:
        img_tags = re.findall(r'<img[^>]+>',html_content)
        return img_tags
    except Exception:
        print('error')
        return []
    
  #function to extract image paths from <img> tags
def IMG_paths(img_tags):
    try:
        img_paths = []
        print("img_tags:",img_tags)
        for img_tag in img_tags:
            src = re.search(r'src=["\'](.*?)["\']', img_tag)
            if src:
                img_paths.append(src.group(1))
        return img_paths  # Move the return statement here
    except Exception as e:
        print("Failed")
        return []


# Function to download and save images
def save_images(base_url, img_paths):
    try:
        for img_path in img_paths:
            # Construct the complete image URL by joining the base_url and img_path
            img_url = base_url + img_path
            print("Image URL:", img_url)
            img_content = download_Html(img_url)
            if img_content:
                # Use os.path.basename to get the filename from the complete URL
                filename = os.path.basename(urlparse(img_url).path)
                with open(filename, 'wb') as file:
                    file.write(img_content)  # Write binary content without encoding
                    print(f"Image '{filename}' downloaded successfully.")
    except Exception as e:
       print("fail")



def main():
    parser = argparse.ArgumentParser(description="Fetch HTML content from a URL using sockets.")
    parser.add_argument("url", nargs="?", default="http://www.google.com", help="URL to fetch HTML content from (default: http://www.google.com)")

    args = parser.parse_args()
    
    #Fetch HTML content from the given URL
    html_content = download_Html(args.url)

    #Initialize filenames list outside of the if statement
    filenames = None

    if html_content:
        #Extract <img> tags from the HTML content
        img_tags = IMG_tags(html_content)
        
        if img_tags:
            #Extract paths from the <img> tags
          img_paths  = IMG_paths(img_tags)
        
          if img_paths:
               #Extract filenames from the paths
              base_url = urlparse(args.url)._replace(path='').geturl()
              print("base_url:",base_url)
              # Save the images locally
              save_images(base_url, img_paths)
                                     
if __name__ == "__main__":
    main()
 