from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

@app.route('/')
@app.route('/login')
def login():
    """
    Renders the login page.
    """
    return render_template('index.html')

@app.route('/register')
def register():
    """
    Renders the registration page.
    """
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """
    Renders the dashboard/books available page.
    In a real app, this would require authentication.
    """
    return render_template('dashboard.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    """
    Handles login requests.
    This is a placeholder. In a real app, you'd validate credentials
    against a database and manage sessions/tokens.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email == 'user@example.com' and password == 'password123':
        flash('Login successful!', 'success')
        
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid email or password.', 'danger')
        return redirect(url_for('login'))

@app.route('/api/register', methods=['POST'])
def api_register():
    """
    Handles registration requests.
    This is a placeholder. In a real app, you'd save user data to a database
    (with hashed passwords).
    """
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')

    if password != confirm_password:
        flash('Passwords do not match.', 'danger')
        return redirect(url_for('register'))

    if len(password) < 6:
        flash('Password must be at least 6 characters long.', 'danger')
        return redirect(url_for('register'))

    print(f"Simulated registration for: Name={name}, Email={email}")
    flash('Registration successful! Please log in.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
