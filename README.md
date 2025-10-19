# Statify

#### Description:
Statify is a web application developed as the final project for Harvard's CS50 course. Its purpose is to provide users with insightful statistics and visualizations about their Spotify listening habits. By connecting to the Spotify Web API, Statify allows users to authenticate with their Spotify account, retrieve their listening data, and explore personalized analytics in a a single-page, simple layout that is user-friendly

## Features

- **Spotify Authentication:** Statify uses OAuth 2.0 to authenticate users with their Spotify account through the spotify API, this allows the app to retrieve the personal insights such as listening habits in a secure way
- **Personalized Dashboard:** After logging in, users are greeted with a dashboard that summarizes their top tracks, artists, and genres in a simple layout
- **Data Visualizations:** The dashboard includes a simple, stylized graph, for the application to have a good, simplistic design and the data to be shown in a much simpler way
- **Responsive Design:** The application is fully responsive, ensuring a seamless experience on both desktop and mobile devices.

## Technical Overview

Statify is built using different web technologies:

- **Frontend:** The user interface is developed with HTML, CSS, and Tailwind CSS for a responsive experience, as well as a modern interface anjoyable to the average user
- **Backend:** The backend is implemented in Python using the Flask framework. It handles user authentication, communicates with the Spotify API, processes data, and serves it to the frontend.
- **Spotify API Integration:** Statify interacts with the Spotify Web API to fetch user data, including top tracks, artists, playlists, and audio features. All API requests are handled securely, and access is processed using the best practices
- **Data Processing:** The backend processes raw Spotify data to generate meaningful statistics and aggregates in JSON format, which are then visualized on the frontend.
- **Deployment:** Statify will be deployed on a cloud platform (as of now). examples: Vercel, AWS, etc..

## How It Works

1. **User Authentication:** When a user visits Statify, they are prompted to log in with their Spotify account. The application requests permission to access the user's listening data.
2. **Data Retrieval:** Upon successful authentication, Statify retrieves the user's top tracks, artists, and playlists from Spotify.
3. **Data Analysis:** The backend processes this data in the /callback route in order to get information about the top tracks, top artists, listening habits, etc...
4. **Visualization:** The processed data is sent to the frontend, where it is displayed using interactive charts and graphs.
5. **User Interaction:** Users can filter see their account data, listening habits, and even change accounts by logging out and in

## Motivation

The motivation to do this project was mainly the spotify wrapped and the mobile app "stats.fm" which served as an inspiration for this project, as well as a guide for implementing the features present in this proyect.

## Challenges and Solutions

Developing Statify involved different kind of challenges:

- **Authentication:** Implementing OAuth 2.0 was a challenge as it needed the configuration of a /callback route and further modifications in teh spotify for developers panel by itself
- **Data Visualization:** Formatting complex data such as large JSON files into summarized, simple information meant a challenge in terms of a deeper understanding in jinja templating
- **Design choices and graphs:** Tailwind CSS was chosen for the development of this project as it allows for a faster, simpler, and more straighforward implementation of the design, however the most difficult part was using chart.js to correctly create a graph that is both informative and visually pleasing

## Future Improvements

Even if this project is directed towards the completion of the CS50, further improvements will be created such as:

- **Social Features:** Allowing users to compare their statistics with friends or share their dashboards on social media.
- **Selection Of Time Ranges:** allowing the user to select a time range for their statistics (such as weekly, monthly, or by year)
- **Export Options:** Enabling users to export their statistics and visualizations as images or PDF reports.
- **Additional Integrations:** Supporting other music platforms beyond Spotify. as for example: Apple Music and Tidal

## Conclusion

Statify represents the culmination of skills learned throughout the CS50 course, including web development, API integration, data processing, and user interface design. It demonstrates the ability to build a full-stack application that solves a real-world problem and delivers value to users. By making music data accessible and engaging, Statify encourages users to explore their musical tastes and discover new favorites.
