#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the mars nasa news site

# In[ ]:


url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')


# In[ ]:


slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


browser.quit()


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1 Scrape High Resolution Mars' Hemisphere Images and Titles

# ### Hemispheres

# In[ ]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# In[ ]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[ ]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Results returned as an iterable list
hemi_images = img_soup.find_all('div', class_='item')
img_soup = soup(html, 'html.parser')

# Loop through returned results
for hemi in hemi_images:
    
    # Retrieve the titles
    title = img_soup.find('h2', class_='title').text
    
    # Get the link to go the full image site
    img_url = 'https://marshemispheres.com/' + str(img_soup.find('img', class_='wide-image')['src'])
    
    # Creating the full_img_url
    full_img_url = main_url + img_url
    
    # Use browser to go to the full image url and set up the HTML parser
    browser.visit(full_img_url)
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Retrieve the full image urls
    hemisphere_img = img_soup.find('div',class_='downloads')
    hemisphere_full_img = hemisphere_img.find('a')['href']
    
    # Creating hemispheres dict
    hemispheres = {'img_url': img_url,'title': title}
  
    #Append the hemisphere_image_urls list
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    # Printing hemisphere_full_img
    print(hemisphere_full_img)


# In[ ]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


browser.quit()


# In[ ]:




