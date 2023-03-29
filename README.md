# NewsRoom

##Project Description:

The project is a Django-based website that displays the latest technology news using an external API. The API provides a JSON file with various values such as the title, source, author, image URL, description, and link to the article.

The application uses the Django framework to create models that represent the data received from the API. The data is stored in an SQLite database, which allows for easy access and manipulation of the data.

The website's homepage displays a list of the latest news articles, sorted by date. Each article is represented by a card that displays the article's title, source, author, and image. Clicking on an article card will take the user to the full article on the source website.

The application also utilizes a cron job to automate the process of fetching the latest news from the API periodically. The cron job runs at regular intervals and updates the database with new articles.

Overall, this project provides a convenient and user-friendly way for people interested in technology news to stay up-to-date with the latest developments in the field.
