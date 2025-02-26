# LaVague News and Weather Dashboard

A simple Flask-based web application that provides news summaries and weather information through agent-based implementation.

# Large Action Model (LAM)
A large action model is a form of AI technology designed to process information and execute actions based on that information. Unlike large language models (LLMs), which primarily focus on understanding and generating language-based outputs, Large action models (LAMs) are capable of performing tangibleactions in the real world.

It is a shift from passive processing to active execution that marks a significant evolution in AI capabilities.

## How Do Large Action Models Work?

Large action models rely on a foundation of data and advanced machine learning techniques to perform their functions. Similar to AI agents, they’re designed to understand complex data inputs and take appropriate actions, making them highly effective across various real-world applications.

LAM AI technology, such as the xLAM series developed by Salesforce AI Research, is designed to enhance the capabilities of AI agents across a variety of tasks. These models incorporate both dense and mixture-of-experts architectures, ranging from 1B to 8x22B parameters. They use a scalable and flexible training pipeline, which allows them to integrate and synthesize diverse datasets, significantly improving the generalizability and performance of AI agents in different environments.

A key component of the LAMs’ training process is data unification, where data collected from multiple sources in various formats is standardized. Standardization reduces noise and simplifies further data processing tasks such as augmentation and quality verification.

For instance, in the xLAM series, data unification involves structuring data in a function-calling format, which consists of modules like task instruction, available tools, and query steps. As a result of this unified format, the model can generalize across different tasks and environments.

Following data unification, data augmentation plays a role in enhancing the diversity of the training data. This involves transforming existing datasets to generate new, synthetic data samples that help prevent model overfitting. Techniques used include prompt format augmentation, where the order of data elements is shuffled, and instruction-following augmentation, which involves rephrasing and verifying task instructions to improve the model’s capability to follow diverse instructions accurately.

## Neuro-symbolic programming

Neuro-symbolic programming is the real secret to how LAMs function. It allows them to process information and understand and execute tasks that require a blend of cognitive understanding and procedural execution. For instance, a LAM might use symbolic reasoning to plan a travel itinerary based on logical rules (like flight times and hotel check-in policies) and neural networks to understand and interpret user preferences and past behavior.

The symbolic part of neuro-symbolic programming helps make the decision-making process of LAMs more transparent and interpretable. In applications where understanding the rationale behind decisions is important, such as in healthcare or finance, this kind of transparency can be useful. When you combine this with neural networks, LAMs achieve a balance of high accuracy and the ability to justify their actions.

The hybrid nature of neuro-symbolic models enables LAMs to generalize across different domains. They can learn from specific instances in one domain and apply learned rules in another, which is beneficial for scaling AI applications across different industries without needing extensive retraining.
## Project Overview

LaVague is a modular web application that consists of agent implementations for retrieving and processing different types of data:

1. **News Summarizer Agent**: Fetches and summarizes headlines from various news sources including Hacker News, BBC, and CNN.
2. **Weather Agent**: Retrieves current weather information for a specified city using the WeatherAPI.

## Features

- Web interface for inputting news URLs and city names
- News headline summarization from popular news sites
- Current weather data display for specified locations
- Modular agent-based architecture for easy extension

## Requirements

- Python 3.12+
- Flask
- BeautifulSoup4
- Requests
- python-dotenv

## Installation

1. Clone the repository:

   ```
   git clone https://gitlab.com/workspace_openai/lam-project.git
   cd lavague_weather
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```
   pip install flask beautifulsoup4 requests python-dotenv
   ```

4. Create a `.env` file in the root directory with your WeatherAPI credentials:

   ```
   WEATHER_API_KEY=your_api_key_here
   WEATHER_API_ENDPOINT=https://api.weatherapi.com/v1/current.json
   ```

## Usage

1. Start the application:

   ```
   python3 web_app.py
   ```

2. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

3. In the web interface:
   - Enter a news URL (e.g., https://news.ycombinator.com/, https://www.bbc.com/news, https://www.cnn.com/) to get a summary of top headlines
   - Enter a city name to get current weather information

## Project Structure

```
lavague_weather/
├── web_app.py             # Main application file with agent implementations
├── .env                   # Environment variables file (create this)
├── templates/             # HTML templates directory
│   └── index.html         # Main interface template
├── static/                # Static files (CSS, JS, etc.)
└── README.md              # This file
```

## Agent Architecture

The application uses a base `LaVague` class that different agents inherit from:

- `NewsSummarizer`: Fetches and parses news headlines from various sources
- `WeatherAgent`: Retrieves weather data for specified locations

This modular design allows for easy extension with additional agent types.

## API Keys

To use the Weather functionality, you'll need to:

1. Sign up for a free account at [WeatherAPI.com](https://www.weatherapi.com/)
2. Get your API key from the dashboard
3. Add it to your `.env` file as shown in the Installation section

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.