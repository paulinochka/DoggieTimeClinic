% rebase('layout.tpl', title=title, year=year)

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/content/bootstrap.css" />
</head>

<body>
    <div class= "divMarginTitle">
        <div class="center">
                <h1 class="titleStyle">Our future events!</h1>
        </div>
        <div class="line"></div>
    </div>

    <div class = "divMargin">
        <div class="eventsRectangleContainer">
            <div class="eventsRectangle">
                <h1 class="eventsStyle">Our visitors</h1>
            </div>
            <div class="eventsRectangle">
                <h1 class="eventsStyle">Our future events!</h1>
            </div>
            <div class="eventsRectangle">
                <h1 class="eventsStyle"></h1>
            </div>
            
        </div>

        <div class= "divMarginTitle">
            <div class="center">
                    <h1 class="titleStyle">Add your event</h1>
            </div>
            <div class="line"></div>
        </div>

        <div class = "divInputMargin">
            <div class="center">
                <div class="form-container">
                    <form action="/events" method="post">
                        <div class="inputRow">
                            <input class="inputStyle" type="text" name="title" placeholder="Whats the name?" required></input>
                            <input class="inputStyle" type="text" name="organiser" placeholder="Who is the organizer?" required></input>
                            <input class="inputStyle" type="text" name="phone" placeholder="Organizers phone number" required></input>
                        </div>
                        <div class="textareaRow">
                            <textarea class="inputStyle" type="text" name="describe" placeholder="Describe the event" required></textarea>
                            <button type="submit" class="middleButton">Send</button>
                        </div>
                    </form>
                </div>
            </div>
    </div>
</body>