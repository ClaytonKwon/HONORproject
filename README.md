# HONORproject
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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Spotify Artist</title>
</head>
<body>
    <h1>Random Spotify Artist</h1>
    <h2>{{ artist.name }}</h2>
    <img src="{{ artist.images[0].url }}" alt="{{ artist.name }}" width="300">
    <p>{{ artist.genres|join(', ') }}</p>
    <a href="{{ artist.external_urls.spotify }}" target="_blank">Listen on Spotify</a>
</body>
</html>
