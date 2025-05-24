# Salesforce CLI (sf) Setup Instructions on Windows

---

## 1. Install Salesforce CLI (sf)

- Download and run the Salesforce CLI installer from:  
  [https://developer.salesforce.com/tools/salesforcecli](https://developer.salesforce.com/tools/salesforcecli)

---

## 2. Copy Binaries (Optional Manual Relocation)

- After installation, navigate to:  
  `C:\Program Files\sf`

- Copy the entire `sf` folder to your Documents folder:  
  `C:\Users\<YourUsername>\Documents\sf`

---

## 3. Update System Environment Variables

- Press `Win + S` and search for **Edit the system environment variables**

- Click on the **Environment Variables** button

---

## 4. Edit the PATH Variable

- Under **System variables** or **User variables**, find the `Path` variable

- Click **Edit**

- Add a new entry:  
  `C:\Users\<YourUsername>\Documents\sf\bin`

> Replace `<YourUsername>` with your actual Windows username.

---

## 5. Confirm Installation

- Open **Command Prompt** or **PowerShell**

- Type:  
  ```bash
  sf --version
