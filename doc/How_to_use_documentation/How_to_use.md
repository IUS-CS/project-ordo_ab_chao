# How to use the software: 
## Home page
There are several different things to use on the home page. First is the "login" and "create account" at the top of the page. It's 
pretty self-explanatory. If you don't have an account, then click on the "create account" link to create a username and password. 
Once the account is created, when the user presses the submit button, it redirects to the login page. The user will then login and 
submitting with the submit button redirects back to the home page. Once on the home page, the user can enter in the keywords to 
search by. Once the 'display_graphs/graphs.html' page displays, you need to go down to the 'Past Sales' dataframe (under the neural network graph) and check for auctions that do not fit with what you want. Then, start excluding certain keywords on the home page by using a dash and then the word that you want exluded. There is a learning curve to typing in the keywords you want and using a dash to exlude certain words thus excluding certain auctions from the 'Past Sales' dataframe that is not wanted. This website mainly caters to expensive high-end collectibles in the categories of: Trading cards, comic books, and coins. Another bonus is that on Ebay, you can only search 'completed items'/'sold listings' up to two months before the current date. The query to Ebay's database allows the user to get up to four months, from the present day, in the past of sold listings. Something exclusive to this website that Ebay's searches do not offer users.
Below are some sample keyword searches to search by:
1. Example of trading cards below. Make sure to include a year, manufacturer, possibly card number, name, professionaly grading 
company and finally a grade consistent with that grader's scale.
#### Example one:
- Type this into the keyword search box: 1979 Topps 18 Gretzky PSA 8
- Below is an example of this
![cards example1 image1](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/cards_example1_how_to_use_1.PNG)
#### This example shows the year (1979), manufacturer (Topps), card number (18), last name (distinct enough to not get different results, as oppose to "smith" being the last name), grading company (PSA), and finally the grade being consistent with their standards (8).
- Now press ENTER and you will be directed to the graphs page. Scroll down and look for the 'Past Sales' dataframe
- Below is an example of what the 'Past Sales' dataframe looks like
![past sales dataframe](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/past_sales_dataframe.PNG)
- Suppose their were unwanted results in the dataframe that are not 1979 Topps Gretzky rookies graded PSA 8??? No you need to learn what keywords are in the title of the sold auction, that are not in any of the titles of sold items you do want, and go back to the Home Page and use the dash operator to exclude certain keywords from the search. Suppose three keywords would get rid of these sold items and wouldn't get rid of any wanted results. The three sample keywords to be excluded from the search are 'reprint', 'redemption' and 'insert'
- Below is an example of using the 1979 Topps 18 Gretzky PSA 8 to get the desired results and using the dash operator to rid the 'Past Sales' dataframe of the three unwanted sold items
![cards example1 image2](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/cards_example1_how_to_use_2.PNG)
- Below are more examples of using keywords to search for rare, professionally graded cards, comic books and coins.
#### Example two:
- 1985 Topps 8a Adam Bomb BGS 9.0
#### This example shows the year (1985), manufacturer (Topps), card number (8a), full name on card (Adam Bomb), grading company (Beckett Grading Service), and grade consistent with their grading scale (9.0).
2. Example of comic books below. Make sure to include a name of comic book (exact title), year, number of comic book, distinct keywords that 
differentiate that comic book from others that are similar in many ways (like first appearance or #1 issue), grading company, and grade 
consistent with that grading companies grading scale.
#### Example one:
- Amazing Fantasy #15 1962 Spider-Man CGC 3.5
#### This example shows the comic book title (Amazing Fantasy), number (#15), year of issue (1962), keyword stipulating "Spider-Man" (significance being its his very valuable first appearance in any comic book), grading company (CGC), and grade in accordance with grading scale at CGC (3.5).
#### Example two:
- Journey into Mystery #83 1962 Thor FA CGC 7.0
#### This example shows the comic book title (Journey into Mystery), number (#83), year of issue (1962), keywords (Thor FA, because it's Thor's first appearance, i.e.- "FA", and origin), grading company (CGC), and grade consistent with grading companies grading scale (7.0).
3. Example of coin below. Make sure to include the year, coin type, mint mark, any other keywords that are relevant, grading company, and the grade of the coin consistent with the grading companies grading scale.
#### Example one:
- 1895 Morgan dollar proof PCGS pr-60
#### This example shows the year (1895), type (Morgan dollar), mint mark not included because it's Philadelphia minted which is the default mint mark in older 19th century coins...so it's not necessary to state that, keywords relevant (proof, it's a proof and not for circulation in general), grading company (PCGS), and grade on encapsulation slab (pr-60).
## Blog
Any user that has an account and is logged in can create a blog. If the user isn't signed in, then the user will be redirecting to the login 
page to login first. Then redirected to the home page after logging in (this needs to be fixed for the blog page). Once signed in, the user 
can read all blogs by everyone. Currently, the search box in the navbar doesn't work. When it does, the search box can be used to sort 
through the blogs based on certain keywords in the title and/or blog message body. A user can also update/edit or delete a blog that was 
created by them (associated with that specific username and password only). Other users cannot edit and delete other user's blog posts.
## Contact page
For now, it just contains only information on how to rearch John Heinz (team leader of "ordo ab chao").
## About Us page
The user can scroll through and see detailed information on everyone in the team. It also contains a link to our team's Github repository 
for this project.
