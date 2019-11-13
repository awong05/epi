"""
Airlines often give customers who fly frequently with them as a "status". This
status allows them early boarding, more baggage, upgrades to executive class,
etc. Typically, status is a function of miles flown in the past twelve months.
People who travel frequently by air sometimes want to take a round trip flight
simply to maintain their status. The destination is immaterial—the goal is to
minimize the cost-per-mile (cpm), i.e., the ratio of dollars spent to miles
flown.

Design a system that will help its users find mileage runs.

Hint: Partition the implied features into independent tasks.

"""

"""
There are two distinct aspects to the design. The first is the user-facing
portion of the system. The second is the server backend that gets flight-price-
distance information and combines it with user input to generate the alerts.

We begin with the user-facing portion. For simplicity, we illustrate it with a
web-app, with the realization that the web-app could also be written as a
desktop or mobile app. The web-app has the following components: a login page, a
manage alerts page, a create an alert page, and a results page. For such a
system we would like defer to a single-sign-on login service such as that
provided by Google or Facebook. The management page would present login
information, a list of alerts, and the ability to create an alert.

One reasonable formulation of an alert is that it is an origin city, a target
cpm, and optionally, a date or range of travel dates. The results page would
show flights satisfying the constraints. Note that other formulations are also
possible, such as how frequently to check for flights, a set of destinations, a
set of origins, etc.

The classical approach to implement the web-app front end is through dynamically
generated HTML on the server, e.g., through Java Server Pages. It can be made
more visually appealing and intuitive by making appropriate use of cascaded
style sheets, which are used for fonts, colors, and placements. The UI can be
made more efficient through the use of Javascript to autocomplete common fields,
and make attractive date pickers.

Modern practice is to eschew server-side HTML generation, and instead have a
single-page application, in which JavaScript reads and writes JavaScript Object
Notation (JSON) objects to the server, and incrementally updates the single-page
based. The AngularJS framework supports this approach.

The web-app backend server has four components: gathering flight data, matching
user-generated alerts to this data, persisting data and alerts, and generating
the responses to browser initiated requests.

Flight data can be gathered via "scraping" or by subscribing to a flight data
service. Scraping refers to extraction of data from a website. It can be quite
involved—some of the issues are parsing the results from the website, filling in
form data, and running the JavaScript that often populates the actual results on
a page. Selenium is a Java library that can programmatically interface to the
Firefox browser, and is appropriate for scraping sites that are rich in
Javascript. Most flight data services are paid. ITA software provides a very
widely used paid aggregated flight data feed service. The popular Kayak site
provides an Extensible Markup Language (XML) feed of recently discovered fares,
which can be a good free alternative. Flight data does not include the distance
between airpports, but there are websites which return the distance between
airport codes which can be used to generate the cpm for a flight.

There are a number of common web application frameworks—essentially libraries
that handle many common tasks—that can be used to generate the server. Java and
Python are very commonly used for writing the backend for web applications.

Persistence of data can be implemented through a database. Most web application
frameworks provide support for automating the process of reading and writing
objects from and to a database. Finally, web application frameworks can route
incoming HTTP requests to appropriate code—this is through a configuration file
matching URLs to methods. The framework provides convenience methods for
accessing HTTP fields and writing results. Frameworks also provide HTTP
templating mechanisms, wherein developers intersperse HTML with snippets of code
that dynamically add content to the HTML.

Web application frameworks typically implement cron functionality, wherein
specified functions are executed at a regular interval. This can be used to
periodically scrape data and check if the condition of an alert is matched by
the data.

Finally, the web app can be deployed via a platform-as-a-service such as Amazon
Web Services and Google App Engine.

"""
