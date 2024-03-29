[Discussion Post (created on 2/9/2021 at 12:55)](https://leetcode.com/problems/long-pressed-name/discuss/1498385/Python-Straightforward-Bruteforce)  
[Discussion Post (created on 16/0/2021 at 4:20)](https://leetcode.com/problems/long-pressed-name/submissions/)  
<h2>925. Long Pressed Name</h2><h3>Easy</h3><hr><div><p>Your friend is typing his <code>name</code> into a keyboard. Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code> characters of the keyboard. Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> name = "alex", typed = "aaleex"
<strong>Output:</strong> true
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> name = "saeed", typed = "ssaaedd"
<strong>Output:</strong> false
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> name = "leelee", typed = "lleeelee"
<strong>Output:</strong> true
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> name = "laiden", typed = "laiden"
<strong>Output:</strong> true
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length &lt;= 1000</code></li>
	<li><code>1 &lt;= typed.length &lt;= 1000</code></li>
	<li><code>name</code> and <code>typed</code> contain only lowercase English letters.</li>
</ul>
</div>