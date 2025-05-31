% for partner, partner_data in partners.items():
    <div class="partnerRectangleLayout">
        <div class ="singleColumn">
            <h1 class = "partnerStyle">{{ partner }}</h1>
        </div>
        <div class="doubleСolumn">
            <div clas = "topItem">
                <h1 class = "partnerStyleDoubleColumnUp">Phone: {{ partner_data['phone'] }}</h1>
            </div>
            <div clas = "bottomItem">
                <h1 class = "partnerStyleDoubleColumnDown">About me: {{ partner_data['description'] }}</h1>
            </div>
        </div>
    </div>
% end