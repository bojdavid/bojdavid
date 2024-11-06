<h1>Documentation for <code>alarm</code> Function</h1>
    <h2>Purpose:</h2>
    <p>The function <code>alarm(seconds)</code> counts down the time from a specified number of seconds, clearing the terminal screen at each interval. Once the timer expires, it plays an alarm sound for a set duration (e.g., 3 seconds).</p>
    
  <h2>Parameters:</h2>
    <ul>
        <li><strong>seconds</strong>: The total time (in seconds) to count down before triggering the alarm.</li>
    </ul>

  <h2>Flow of Execution:</h2>
    <ol>
        <li><strong>Countdown:</strong>
            <p>The screen is cleared using invisible characters (<code>\033[2J</code>), and the timer starts counting down from the specified number of seconds. The remaining time is displayed in the format <code>mm:ss</code>, where <code>mm</code> represents minutes and <code>ss</code> represents seconds. The countdown updates every second.</p>
        </li>
        <li><strong>Alarm Sound:</strong>
            <p>When the countdown reaches zero, the alarm sound (<code>alarm.wav</code>) is loaded and played. The sound plays for 3 seconds, and then it is stopped.</p>
        </li>
    </ol>

  <h2>Dependencies:</h2>
    <ul>
        <li><code>simpleaudio</code>: Used for playing the <code>.wav</code> file.</li>
        <li><code>time</code>: Used for implementing the countdown functionality and controlling the delay between updates.</li>
    </ul>

  <h2>Example Usage:</h2>
    <pre><code>
alarm(10)  # Starts a 10-second countdown, followed by playing an alarm sound.
    </code></pre>
