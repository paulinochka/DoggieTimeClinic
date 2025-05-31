% for event, event_data in events.items():
    <div class="eventsRectangle" onclick="showEventDetails(this, '{{ event }}')">
        <h1 class="eventsStyle">{{ event }}</h1>
        <div class="event-details" style="display: none;">
            <p><strong>Organiser:</strong> <span class="organiser">{{ event_data['organiser'] }}</span></p>
            <p><strong>Phone:</strong> <span class="phone">{{ event_data['phone'] }}</span></p>
            <p><strong>Description:</strong> <span class="description">{{ event_data['description'] }}</span></p>
        </div>
    </div>
% end