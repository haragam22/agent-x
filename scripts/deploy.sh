echo "Starting deployment process..."

# Navigate to the project directory (update with actual path)
cd C:\Users\hp\blockchain\agentx || exit

# Pull the latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull origin main

# Activate virtual environment (if applicable)
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations (if using Django or Flask with SQLAlchemy)
if [ -f "manage.py" ]; then
    echo "Running Django migrations..."
    python manage.py migrate
fi

# Restart application (adjust for your setup)
echo "Restarting application..."
pkill -f "agentx"  # Stop any running instances
nohup python main.py &  # Run the app in the background

echo "Deployment completed successfully!"
