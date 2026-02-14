<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Project Name] 🎯

## Basic Details

### Team Name: [Eclipse]

### Team Members
- Member 1: [Anagha S S] - [LBSITW]
- Member 2: [Anannya I] - [LBSITW]

### Hosted Project Link
[https://doblo-3.onrender.com/]

### Project Description
[In the world of emergency medicines, the difference between a life saved and a life lost is often measured in minutes.While the total number of potential donors is often sufficient, the lack of unified,real time co-ordination leads to delay in life saving trasfusions.A platform that act as the real time bridge between those in urgent need of blood and a verified network of local donors.Matching and tiered urgency levels, Health vault, eligibility tracker, location privacy and smart notification system are our key features.Donors are gifted with different levels of hero badges to add to the uniqueness of the platform]

### The Problem statement
[In the world of emergency medicines, the difference between a life saved and a life lost is often measured in minutes.While the total number of potential donors is often sufficient, the lack of unified,real time co-ordination leads to delay in life saving trasfusions.]

### The Solution
[A platform that act as the real time bridge between those in urgent need of blood and a verified network of local donors.Matching and tiered urgency levels, eligibility tracker, location privacy and smart notification system are our key features.Donors are gifted with different levels of hero badges to add to the uniqueness of the platform]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [ HTML, Python, css]
- Frameworks used: [Flask]
- Libraries used: [sqlite3, datetime]
- Tools used: [ VS Code, Git,Git hub]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

List the key features of your project:
- Matching blood types with tiered urgency levels
- Donor eligibility tracker
- Smart notifications for requests
- Privacy‑protected donor information
- Hero badge system for donors



---

## Implementation

### For Software:

#### Installation
```bash
[Installation commands -pip install -r requirements.txt]
```

#### Run
```bash
[Run commands -python app.py]
```


---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

!["C:\Users\Anagha S S\Desktop\Photo\start.png"]
*starting interface of DoBlo*

!["C:\Users\Anagha S S\Desktop\Photo\donor.png"]
*Donor registration*

!["C:\Users\Anagha S S\Desktop\Photo\eligibility.png"]
*donor eligibility notification*

!["C:\Users\Anagha S S\Desktop\Photo\request.png"]
*blood donor request*

!["C:\Users\Anagha S S\Desktop\Photo\matching.png"]
*donor matching using database*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

!["C:\Users\Anagha S S\Desktop\Photo\work flow diagram.png"]
*two options are there in the beginning whether the user is a donor or someone needing blood. The donor details are collected and stored in database for future use.When a person requests blood te data from database is used for fetching and matching the suitable donor*

---



---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

!["C:\Users\Anagha S S\Desktop\Photo\Doblo navigation structure.png"](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---


---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python app.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[https://drive.google.com/file/d/1wZozSbNCDynmszkFNmlQcgf2bbbrDfuY/view?usp=drive_link]

*The video demonstrates the working of DoBlo website. How the donor registration and blood request are carried out*



---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [lenovo copilot, gemini, chatgpt]

**Purpose:** [What you used it for]
- Debugging deployment errors (Render port binding issue)
- Writing documentation
- UI improvement suggestions
- Git conflict troubleshooting
**Key Prompts Used:**
"Fix Render port scan timeout error"

"Create DoBlo website README"

"Resolve Git unrelated histories error"

**Percentage of AI-generated code:** [Approximately 35%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Anagha S S]: [- Designed and implemented the backend logic using Flask
- Created the SQLite database schema for donor registration and request matching
- Developed the eligibility tracker rules (age, weight, donation history, medical conditions)
- Integrated donor registration with duplicate detection (name + DOB + phone)]
- [Anannya I]: [- Designed and implemented the backend logic using Flask
- Created the SQLite database schema for donor registration and request matching
- Developed the eligibility tracker rules (age, weight, donation history, medical conditions)
- Integrated donor registration with duplicate detection (name + DOB + phone)]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
