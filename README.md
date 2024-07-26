# streamlit_microlearning_template

## Project Description
A Streamlit template to create a microlearning session application.It can be also a good way to show a report.

## Features
- **App based on sections**: Each section has content that can be with or without questions, with controls to verify if answers are correct, advance, go back and if the microlearning session is finished.
- **Section elements**:
  - Text
    - Title
    - Text
  - Media
    - Image
    - Lottie animation
    - Another Python script
  - Questions
    - Single answer question
    - Multiple answers question
  - Explanations
- **Sidebar for additional information**
- **Last section for congratulations and additional information**

## Installation Instructions
To install and run the app, follow these steps:
1. Clone the repository from [GitHub](https://github.com/benderpt/streamlit_microlearning_template) and fork it.
2. Install the required dependencies listed in `requirements.txt`.

```bash
git clone https://github.com/benderpt/streamlit_microlearning_template.git
cd streamlit_microlearning_template
pip install -r requirements.txt
```
3. Run the Streamlit app.
```bash
streamlit run app.py
```

## Dependencies
List of dependencies required is available in `requirements.txt`.

## File Structure
An overview of the main files and directories in your project:

- `sections_structure.json`: This file controls the content and parameters of each section.
- `scripts/components.py`: This is a boilerplate file with the functions that control the sections elements behavior.
- `scripts/endsection.py`: This file controls the content of the last section.
- `scripts/sidebar.py`: This file controls the sidebar.
- `app.py`: This is the file to run the app.

## Usage Instructions
To develop your microlearning from this template, you should have a microlearning session organized, with media, title, content, and questions.

The `sections_structure.json` file should be edited in which each item represents a section of the session.

### Fields available:

- **title**: String field for the title of the section.
- **text**: String of text for the session.
- **lottie**: Path to the Lottie animation file.
- **image_path**: Path to the image file used in the section.
- **script_path**: Path to the script file executed in the section.
- **question_multiple**: String for the multiple-choice question.
- **question**: String for the single selection question asked in the section.
- **options**: Array of strings representing multiple-choice options.
- **answer**: A string or array of strings representing correct answers.
- **explanations**: Object containing detailed explanations of various aspects (key-value pairs).
- **button_text**: Text for the button displayed in the section.

Your session media can be stored in the `content/Assets` folder.

In the `scripts` folder, you should edit `sidebar.py` and `endsection.py` scripts to customize information. Also in the `scripts` folder, you should add any script you want for a particular section, using `script_path` in the JSON to link.

## Contributing

Contributions are welcome and greatly appreciated. Here's how you can contribute:

1. Fork the project repository.
2. Create a new feature branch (`git checkout -b feature/YourAmazingFeature`).
3. Commit your changes (`git commit -m 'Add some YourAmazingFeature'`).
4. Push to the branch (`git push origin feature/YourAmazingFeature`).
5. Open a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- [LinkedIn](https://www.linkedin.com/in/hugoalmeidamoreira/)
- [Email](mailto:hugoalmeidamoreira@gmail.com)
