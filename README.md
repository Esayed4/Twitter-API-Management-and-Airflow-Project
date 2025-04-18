
# Twitter API Management and Airflow Project

This project is designed to interact with the Twitter API for extracting tweets based on specified constraints. It combines API management scripts with an Apache Airflow DAG to monitor and manage API request history.

## Project Structure

<h1>Twitter API Management and Airflow Project</h1>

<p>This project is designed to interact with the Twitter API for extracting tweets based on specified constraints. It combines API management scripts with an Apache Airflow DAG to monitor and manage API request history.</p>

<h2>Project Structure</h2>
<pre>
/project-root
│
├── api_management/
│   ├── AI_Al_Azhar.json           # JSON data related to the Al Azhar query.
│   ├── API_History.csv             # Logs the history of API requests.
│   ├── API_file.json               # Configuration for available APIs and their limits.
│   ├── Choice_Apis.py              # Logic for selecting which APIs to use.
│   ├── Constrains_Data.json        # Constraints for API queries.
│   ├── modify_the_api_tweets_file.py # Script to modify API usage history.
│   ├── Extract_Data.py             # Script for extracting data from Twitter.
│   └── written_var.txt             # Contains variable names used in the project.
│
└── airflow_code/
    ├── monitor_api_history.py       # Main DAG file for monitoring API history.
    ├── API_file.json                # Configuration for available APIs.
    ├── API_History.csv              # Logs of API requests.
    └── [Other necessary files]
</pre>

<h2>Installation</h2>

<h3>Requirements</h3>
<p>Make sure you have the following installed:</p>
<ul>
    <li>Python 3.x</li>
    <li>Apache Airflow</li>
    <li>Pandas</li>
    <li>Requests</li>
</ul>

<p>You can install the required Python packages using:</p>
<pre><code>pip install apache-airflow pandas requests</code></pre>

<h2>Usage</h2>

<h3>API Management</h3>
<ol>
    <li><strong>Set Up API Management</strong>:
        <ul>
            <li>Open  the hole api_management folder.</li>
            <li>Modify <code> Constrains_Data.json</code> to put your constrains</li>
            <li>Modify <code> API_file.json</code> to put your own apis</li>
            <li>Modify <code>Choice_Apis.py</code> to set the number of wanted tweets and other parameters.</li>
            <li>Execute <code>Extract_Data.py</code> to start the data extraction process.</li>
        </ul>
    </li>
</ol>

<h3>Airflow DAG</h3>
<ol>
    <li><strong>Set Up Airflow</strong>:
        <ul>
            <li>Initialize the Airflow database:
                <pre><code>airflow db init</code></pre>
            </li>
            <li>Start the Airflow web server:
                <pre><code>airflow webserver --port 8080</code></pre>
            </li>
            <li>Start the Airflow scheduler in another terminal:
                <pre><code>airflow scheduler</code></pre>
            </li>
        </ul>
    </li>
    <li><strong>Deploy the DAG</strong>:
        <ul>
            <li>Modify<code>docker-compose-yaml</code> in your Airflow in line 80 to put the url of the <code>API_History.csv</code> and <code> API_file.json</code> </li>
        </ul>
    </li>
    <li><strong>Access the Airflow UI</strong>:
        <ul>
            <li>Open your browser and navigate to <code>http://localhost:8080</code>.</li>
            <li>You should see the <code>monitor_the_api_history_per_day</code> DAG listed.</li>
        </ul>
    </li>
    <li><strong>Trigger the DAG</strong>:
        <ul>
            <li>You can manually trigger the DAG from the Airflow UI or wait for the scheduled interval (daily).</li>
        </ul>
    </li>
</ol>

<h2>DAG Overview</h2>

<h3>Tasks</h3>
<ul>
    <li><code>read_api_history</code>: Reads the API history from <code>API_History.csv</code>.</li>
    <li><code>read_api_from_more_than_month</code>: Extracts APIs used more than 31 days ago.</li>
    <li><code>read_api_from_less_than_or_equal_month</code>: Extracts APIs used within the last 31 days.</li>
    <li><code>read_the_api_file_and_add_requests</code>: Updates the available requests in <code>API_file.json</code> based on historical usage.</li>
    <li><code>write_the_new_api_history</code>: Writes the current API history back to <code>API_History.csv</code>.</li>
</ul>

<h3>Dependencies</h3>
<p>The tasks are linked in a sequence to ensure that data is processed correctly. Each task pushes data to the next task using XComs.</p>

<h2>Configuration</h2>
<ul>
    <li>The API configurations can be found in <code>API_file.json</code>.</li>
    <li>Constraints for data extraction are specified in <code>Constrains_Data.json</code>.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

<h2>Acknowledgments</h2>
<ul>
    <li>Twitter API documentation</li>
    <li>Apache Airflow documentation</li>
    <li>Pandas documentation</li>
</ul>

<h2>Contact</h2>
<p>For questions or contributions, please contact [Your Name] at [Your Email].</p>

</body>
</html>
