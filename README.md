# Refresh your ERDDAP experience

This how-to guide will take your ERDDAP from the blue-and-orange default to something streamlined, specific, and useful (just like this!):

[<img src="https://github.com/user-attachments/assets/7c0341b7-635a-4640-b884-034b4cc9a2c4"/>](https://data.pmel.noaa.gov/pmel/erddap/index.html)


## To update your ERDDAP (the insides):
<ol>
  <li><p>Update your ERDDAP to the <a href="https://erddap.github.io/#latest-erddap-version">most recent version</a> (≥v2.25, see top of linked page). Make sure that your setup.xml includes the line <code>&lt;useSaxParser&gt;true&lt;/useSaxParser&gt;</code>.</p></li>
  <li><p>On the same server from where you run your ERDDAP, make a new directory. This will be used as your main workspace for all ERDDAP data, so let's call it ~/erddap_[ERDDAP_NAME]. This should be separate from your tomcat directory.</p></li>
  <li><p>In ~/erddap_[ERDDAP_NAME], save a copy of your current datasets.xml. I like to save this with the date copied, so the file is named [ERDDAP_NAME]_datasetsxml_YYYYMMDDcopy.xml.</p></li>
  <li><p>Next, you'll want to separate out your [ERDDAP_NAME]_datasetsxml_YYYYMMDDcopy.xml so we can reorganize it. First, make a subdirectory for where you want your xml fragments to go. Then, run <code>separate_datasetsxml.py</code>, which will take all of the &lt;dataset&gt; xml fragments and save them into individual files, each named with their datasetID. Then, save the first section of [ERDDAP_NAME]_datasetsxml_YYYYMMDDcopy.xml into a file named first.xml; this should be the very start of the file up until the first <code>&lt;dataset&gt;</code> tag. Make sure that the second line reads: <code>&lt;erddapDatasets xmlns:xi="http://www.w3.org/2001/XInclude"&gt;</code> . Finally, make a file named last.xml, which is everything after the last &lt;/dataset&gt; in [ERDDAP_NAME]_datasetsxml_YYYYMMDDcopy.xml. This is usually the single line <code>&lt;/erddapDatasets&gt;</code>. Save both of these in your ~/erddap_[ERDDAP_NAME] directory.</p></li>
  <li><p>Next, run transitiondatasets_xinclude.py, which takes the filenames of all of your xml fragments and reformats them into one file (xinclude_xml.xml). This file takes the place of the majority (all the <code>&lt;dataset&gt;</code> tags) of the datasets.xml file, reformatting them into the XInclude format (<code>&lt;xi:include href="~/PATH/datasetID.xml"/&gt;</code>). You can then concatenate together first.xml, xinclude_xml.xml, and last.xml into a single file and then copy that to your tomcat directory as datasets.xml. Alternatively, you can run make_datasetsxml.sh, which does all of those steps for you.</p></li>
</ol>
That's it! Now your ERDDAP is up-to-date and easier to use. The next time you need to add a dataset, simply make a new [datasetID].xml file in your subdirectory and run make_datasetsxml.sh. When you edit a dataset's xml, all you need to do is edit the xml fragment.
<br>If all goes well, you will never touch datasets.xml again.

## To update your ERDDAP (the outside):
<ol>
  <li><p>The first and easiest file to edit is first.xml, found in ~/erddap_[ERDDAP_NAME]. You can explore <a href="https://github.com/e-koukel/erddap_instruction/blob/main/first.xml">the example</a> for the screenshot above. 
    <ol>
      <li>The most prominent item to edit in your ERDDAP is the banner at the top of the screen that runs across all pages of your ERDDAP. In first.xml, scroll down to <code>&lt;startBodyHtml5&gt;</code>. You can edit <code>background-color</code> in the second line (the first <code>&lt;table&gt;</code> element). This defaults to #128CB5 and is the color of the banner that spans across the top of each page on your ERDDAP.</li>
      <li>Next, you can edit the <code>&lt;td&gt;</code> elements, starting on the fourth line of <code>&lt;startBodyHtml5&gt;</code>. The first <code>&lt;td&gt;</code> element determines the size and image on the far left of the ERDDAP banner. You can change the hyperlink, image, image size, image margin, and alternate text of this image in this element. To change the image used, edit <code>src="&erddapUrl;/images/noaab.png"</code> to be the name of the actual png that you want, which is located at ~/tomcat/webapps/erddap/images/.</li>
        <li>The second <code>&lt;td&gt;</code> element determines the text within the ERDDAP banner. By default, this reads as "ERDDAP" in large font and "Easier access to scientific data" in a small font underneath. You can change the text and font size here.</li>
        <li>The third  <code>&lt;td&gt;</code> element defines the hyperlinks on the far right side of your ERDDAP banner, and by default read as: Brought to you by NOAA NMFS SWFSC ERD. You can update these to be specific to your institution. I also add <code>class="bannerlink"</code> within each link, which ensures that the links will remain as your desired color even when they've been clicked on (once you follow step 2).</li>
        <li>Next, I recommend adding a <code>&lt;theShortDescriptionHtml&gt;</code> section, like so:
  <pre><code>&lt;theShortDescriptionHtml&gt;
&lt;h1&gt;ERDDAP&lt;/h1&gt;
&amp;erddapIs;                                                                          
&amp;thisParticularErddap;                                                              
[standardShortDescriptionHtml]                                                          
&lt;/theShortDescriptionHtml&gt;</code></pre>
          This will grab the correct information from your messages.xml that we will edit in a later step, which affects the text on the lefthand side of your ERDDAP's homepage.</li>
    </ol>
  </p></li>
  <li><p>The next file to edit is your .css file, found in the ~/tomcat/content/erddap/images/ directory. This is usually called erddapStart2.css or something similar. First, rename the time to erddap2.css. Technically, anything here can be changed, but I would recommend these changes:
    <ol>
      <li>If you'd like, change the color of all links and visited links on your ERDDAP by changing the color designation in your <code>a:link</code> and <code>a:visited</code> items. Then, to keep the links in your ERDDAP banner to remain a chosen color even if they have been visited, add this line below the <code>a:hover</code> line: <code>a.bannerlink {text-decoration:none; color:#FFFFFF;}</code>, with the color chosen being white.</li>
      <li>To change the color of the first text on the right side of the homepage ("Start Using ERDDAP: Search for Interesting Datasets") as well as each dataset's title on the Data Access Form, change the color in the line <code>span.standoutColor {color:#dd5500; }</code></li>
      <li>To change the color of default tables in ERDDAP, go to <code>table.commonBGColor {background-color:#ffffcc; }</code> and change the background-color. If you want alternating background colors for each line in the table, also add the line <code>table tr:nth-child(even) {background:#FFFFFF; }</code>, which affects the color of all the even-numbered lines in ERDDAP's tables.</li>
      <li>To change the color of the vertical line down the center of ERDDAP's homepage, edit the color in the line <code>td.verticalLine {border-left:1px solid #bbbbbb; height:100%; }</code>. I like this to be the same color as the ERDDAP banner.</li>
    </ol>
  </p></li>
  <li><p>The final step is updating your ERDDAP's look and feel is editing the messages.xml file. This is found in the ~/tomcat/webapps/erddap/WEB-INF/classes/gov/noaa/pfel/erddap/util/ directory and affects the text on the lefthand side of ERDDAP's homepage.
  <ol>
    <li><code>&lt;erddapIs&gt;</code> is the text for the first part of the top paragraph on the lefthand side of ERDDAP's homepage. This sentence defaults to starting with "ERDDAP is…". Edit this how you like.</li>
    <li><code>&lt;thisParticularErddap&gt;</code> is the text for the second half of the top paragraph on the lefthand side of ERDDAP's homepage. This sentence defaults to beginning with "This particular ERDDAP installation…" and can be changed however you'd like. I prefer to include information about who runs this ERDDAP and what kind of data it stores.</li>
    <li><code>&lt;standardShortDescriptionHtml&gt;</code> is the text for everything below the first paragraph on the lefthand side of ERDDAP's homepage; this defaults to "Easier Access to Scientific Data" as a heading and also controls all the text below. Edit this however you like.</li>
  </ol>
  </p></li>
</ol>
And you're done! Obviously, ERDDAP offers much more customization than I've listed here, but following these simple steps should revitalize your ERDDAP use and make it stand out from the crowd.
<br>
<hr>
Confused about any of the above? Contact <a href="mailto:ellen.koukel@noaa.gov">Ellen Koukel</a> or consult the official <a href="https://erddap.github.io/">ERDDAP documentation</a>.
