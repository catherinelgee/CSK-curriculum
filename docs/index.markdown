---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
#  CS KICKSTART 2020
---

## CSK @ Berkeley
Jump to <a href="#CONTENT">content</a>, <a href="#RESOURCES">resources</a>, <a href="#QUESTIONS">feedback</a>

---
<a id="CONTENT"></a>
## Content
- This schedule is tentative and due to change

### Announcements
- For those who want a recap or review on the first EE lecture Michelle has offered to teach the material from Tuesday! (it's the same time as EE II as EE II builds on EE I)
- Fill our [project showcase slides](https://docs.google.com/presentation/d/1EA-pLOa1KCohFCdgugLZR34pbxQfv7Y5JC-2794wweM/edit?usp=sharing) by showcase tomorrow

<table>
  {% for row in site.data.contentdata %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {% if pair[0] == "Resources" %}
        {% assign links = pair[1] | split: ' ' %}
        {% for link in links %}
          {% assign linktext = link | split: '|' %}
          <a href="{{ linktext[0] }}">{{ linktext[1] }}</a><br>
        {% endfor %}
      {% else %}
        {{ pair[1] }}
      {% endif %}
    {% endtablerow %}
  {% endfor %}
</table>

---
<a id="RESOURCES"></a>
## Resources
Here is a list of resources that's not directly our course materials that you might find helpful in learning more about the topics that we cover, as well as Berkeley as a whole!
- Extra Practice: some extra problems I have collated that you can do in your free time (lol)
- EE/CS/DS first semester class links:
    - [DATA8](data8.org): Introductory course to data science
        - [CS88](https://cs88-website.github.io/): this is a course meant to replace 61A for a data science intended major/minor
    - [CS10](https://cs10.org/): Intro CS class for those with no prior experience (take before CS61A)
    - [CS61A](https://cs61a.org/): Intro CS class
    - [EECS16A](http://inst.eecs.berkeley.edu/~ee16a/): Intro EE class
- [HKN](https://hkn.eecs.berkeley.edu/): Useful for looking for past exams as well as course tracks you can take
- [AWE Guide to Declaring CS](https://awe.berkeley.edu/2020/04/23/guide-to-declaring-cs/)

---
<a id= "QUESTIONS"></a>
## Feedback
If there are any questions about curriculum on this website you can direct any and all emails to either [cskickstart@gmail.com](mailto:cskickstart@gmail.com) or [catherinegee@berkeley.edu](mailto:catherinegee@berkeley.edu)

If you would like to do this in an anonymous fashion you can fill out [this form](https://forms.gle/xeiKVLnGqBDeQv3u9) as well.
