<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Preload Example</title>

    <!-- Preload CSS -->
    <link rel="preload" href="styles.css" as="style">
    
    <!-- Preload JavaScript -->
    <link rel="preload" href="script.js" as="script">
    
    <!-- Preload an image -->
    <link rel="preload" href="image.jpg" as="image">
    
    <!-- Preload a font -->
    <link rel="preload" href="font.woff2" as="font" crossorigin="anonymous">

    <!-- Normal stylesheet -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Preload Example</h1>
    
    <p>This is a simple web page with preloaded resources.</p>

    <!-- Normal script -->
    <script src="script.js"></script>
</body>
</html>