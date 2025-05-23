% rebase('layout.tpl', title=title, year=year)
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/content/bootstrap.css" />
</head>

<body>
    <div class= "divMarginTitle">
        <div class="center">
                <h1 class="titleStyle">Our partners!</h1>
        </div>
        <div class="line"></div>
    </div>

    <div class = "divInputMargin">
        <div class="center">
            <div class="partnersListContainer">
                <div class="partnersListChange">
                    <h1 class="partnerStyle">Gavgavka</h1>
                </div>
            </div>
        </div>

        <div class= "divMarginTitle">
            <div class="center">
                    <h1 class="titleStyle">Do you want to become a partner?</h1>
            </div>
            <div class="line"></div>
        </div>

        <div class = "divInputMargin">
            <div class="center">
                <div class="form-container">
                    <form action="/events" method="post">
                        <div class="center">
                            <div class="inputRow">
                                <input class="inputStyle" type="text" name="name" placeholder="Whats your name?" required></input>
                                <input class="inputStyle" type="text" name="phone" placeholder="Whats your phone number?" required></input>
                            </div>
                        </div>
                        <div class="center">
                            <div class="textareaRow">
                                <textarea class="inputStyle" type="text" name="describe" placeholder="Tell us about yourself" required></textarea>
                                <a type="submit" class="middleButtonPartner"><span>Send</span></a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
    </div>
</body>