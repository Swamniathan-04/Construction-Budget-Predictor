# 🚀 Deployment Guide for Streamlit Community Cloud

## 📋 Prerequisites

1. **GitHub Account** - You need a GitHub account
2. **Git Installed** - Install Git from https://git-scm.com/
3. **GitHub Desktop** (Optional) - For easier repository management

## 🔧 Step-by-Step Deployment

### Step 1: Install Git
Download and install Git from: https://git-scm.com/downloads

### Step 2: Create GitHub Repository
1. Go to https://github.com
2. Click "New repository"
3. Name it: `Construction-Budget-Predictor`
4. Make it **Public** (required for Streamlit Community Cloud)
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### Step 3: Upload Your Code
**Option A: Using GitHub Desktop (Recommended)**
1. Download GitHub Desktop from https://desktop.github.com/
2. Install and sign in with your GitHub account
3. Click "Clone a repository from the Internet"
4. Select your new repository
5. Choose a local path
6. Copy all your project files to this folder
7. In GitHub Desktop, you'll see all your changes
8. Add a commit message like "Initial commit: Construction Budget Predictor"
9. Click "Commit to main"
10. Click "Push origin"

**Option B: Using Command Line**
```bash
# Navigate to your project folder
cd "D:\Github Repos\Construction-Budget-Predictor"

# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Construction Budget Predictor"

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Construction-Budget-Predictor.git

# Push to GitHub
git push -u origin main
```

### Step 4: Deploy to Streamlit Community Cloud
1. Go to https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `Construction-Budget-Predictor`
5. Set the main file path: `predict_with_ui.py`
6. Click "Deploy"

## ✅ Verification
- Your app will be available at: `https://your-app-name.streamlit.app`
- The deployment process takes 2-5 minutes
- You can monitor the deployment logs

## 🔄 Updates
To update your deployed app:
1. Make changes to your local files
2. Commit and push to GitHub
3. Streamlit will automatically redeploy

## 🐛 Troubleshooting

**Issue: "App not found"**
- Make sure your repository is public
- Check that `predict_with_ui.py` exists in the root directory

**Issue: "Dependencies not found"**
- Verify `requirements.txt` is in the root directory
- Check that all dependencies are listed correctly

**Issue: "Model file not found"**
- Make sure `construction_budget_model.pkl` is included in your repository
- The model file should be in the root directory

## 📞 Support
- Streamlit Community Cloud docs: https://docs.streamlit.io/streamlit-community-cloud
- GitHub help: https://help.github.com/ 