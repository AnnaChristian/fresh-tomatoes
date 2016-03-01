import webbrowser
import os
import re


# Page head; styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">

        <title>Fresh Tomatoes!</title>

        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

        <!-- Custom styles for this template -->
        <link href="styles/normalize.css" rel="stylesheet">
        <link href="styles/album.css" rel="stylesheet">
        <script src="js/default.js"></script>
    </head>
'''


# The main page layout
main_page_content = '''
    <body>

        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
          <div class="modal-dialog">
            <div class="modal-content">
              <span class="hanging-close close-video" data-dismiss="modal" aria-label="Close video">
                <span class="glyphicon glyphicon-remove-circle" aria-hidden="true"></span>
              </span>
              <div class="scale-media" id="trailer-video-container">
              </div>
            </div>
          </div>
        </div>

        <!--  JUMBO -->
        <section class="jumbotron text-xs-center">
          <div class="container">
            <h1 class="jumbotron-heading">Fresh Tomatoes</h1>
            <p class="lead text-muted">Movies project</p>
          </div>
        </section>

        <!-- Main Page Content -->
        <div class="album text-muted">
          <div class="container">
              {movie_tiles}
          </div>
        </div>

    </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-12 col-md-6   movie-tile ">
	<div class="inner-tile">
		<h2 class="text-center">{movie_title}</h2>
		<div class="row">
			<div class="col-xs-12 col-md-6">
				<img class="thumbnail" src="{poster_image_url}"  alt="{movie_title} poster">
			</div>
			<div class="col-xs-12 col-md-6">
				<p>{story}</p>
				<button id="show-video" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><span class="glyphicon glyphicon-play-circle"></span> Play</button>
			</div>
		</div>
	</div>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None
        )

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            story=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_album.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

