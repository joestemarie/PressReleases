import re

press_release = """WASHINGTON, DC – Congressman John Boehner (R-West Chester) today released the following statement in response to the final 2015 federal exchange insurance premium rates, as confirmed by the Ohio Department of Insurance:

“Another day, another story about how the president’s health care law is – once again – driving up insurance costs in Ohio for everyone from families to small businesses,” Boehner said.  “Unfortunately, we’ve seen this coming – between the local horror stories and the multiple reports and studies coming out of the Ohio Department of Insurance.  In just two years, Ohioans have now seen their insurance premiums spike by 53 percent on average – it’s simply unconscionable.  So what more does the president and his Democratic allies in Washington need to see before they admit that this disastrous law is not – as they like to put it – ‘working?’  Every story that piles on further strengthens my resolve to continue fighting to repeal this law and start over with patient-centered reforms that will actually lower health care costs and protect jobs.”

NOTE: The Ohio Department of Insurance confirms that the 2015 premium rate for the individual market will average $372.86, a 12 percent increase over 2014; the 2015 premium rate for small group will average $448.55, a 12 percent increase over 2014.

CLICK HERE for Congressman Boehner’s statement in May 2014, when it was previously predicted that Ohio’s 2015 premium rates would increase over the 2014 rates."""

import unicodedata
unicodedata.normalize('NFKD', press_release).encode('ascii','ignore')

quote = re.findall(r'"([A-Z].+),"|"([A-Z].+)\."',press_release)
print quote

match_date = re.search(r'([A-Z][a-z]+) ([0-3]?[0-9]), ([1-2][0-9]+)',press_release)
month = match_date.group(1)
day = match_date.group(2)
year = match_date.group(3)

print month
print day
print year