<head>
    <title>Vet Clinic</title>
    <link rel="stylesheet" href="\static\content\active.css">
</head>
<body>
    <div class="container">
        <div class="form-container">
            <h1>Ask the Vet</h1>
            <form method="POST" action="/active">
                <div class="form-group">
                    <label>Name:</label>
                    <input type="text" name="name" value="{{name}}" required>
                    % if 'name' in errors:
                        <span class="error">{{errors['name']}}</span>
                    % end
                </div>

                <div class="form-group">
                    <label>Email:</label>
                    <input type="text" name="email" value="{{email}}" required>
                    % if 'email' in errors:
                        <span class="error">{{errors['email']}}</span>
                    % end
                </div>

                <div class="form-group">
                    <label>Phone:</label>
                    <input type="text" name="phone" value="{{phone}}" required>
                    % if 'phone' in errors:
                        <span class="error">{{errors['phone']}}</span>
                    % end
                </div>

                <div class="form-group">
                    <label>Question:</label>
                    <textarea name="question" required>{{question}}</textarea>
                    % if 'question' in errors:
                        <span class="error">{{errors['question']}}</span>
                    % end
                </div>

                <button type="submit">Send</button>
            </form>
        </div>

     
        <div class="questions-container">
            <h2>Recent Questions</h2>
            % if not questions:
                <p class="no-questions">No questions yet.</p>
            % else:
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Question</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for q in questions:
                            <tr>
                                <td>{{q['name']}}</td>
                                <td>{{q['question']}}</td>
                            </tr>
                        % end
                    </tbody>
                </table>
            % end
        </div>
    </div>
</body>
