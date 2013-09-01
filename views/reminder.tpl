<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='roller.css') }}">
</head>
<body id="index"
    %if background_color != "":
        style="background-color:{{ background_color }};"
    %end
    >
  <p id="reminder"
      %if color !="":
          style="color:{{ color }};"
      %end
      >{{ reminder }}</p>
</body>
</html>
