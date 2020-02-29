import time
from collections import Counter
#time.strptime("December 05, 2010, 09:08:08 AM","%B %d, %Y, %I:%M:%S %p")
f=open("Satoshi.txt")

fields=[]
time_result=[]
week_result=[]
for line in f:
	for word in line.split("', 'on: "):
			fields.append(word.replace("'on: ",""))
for str in fields:
	try:
		time_result.append(time.strptime(str,"%B %d, %Y, %I:%M:%S %p").tm_hour)
		week_result.append(time.strptime(str,"%B %d, %Y, %I:%M:%S %p").tm_wday)
	except Exception as e:
		print(e)
list3=["{}-{:02}".format(a_,b_) for a_,b_ in zip(week_result,time_result)]#[list(a) for a in zip(week_result,time_result)]
print(list(set(time_result)))
print(Counter(time_result))	
print(Counter(week_result))
print(Counter(list3))
'''
rue identity of Satoshi Nakamoto being revealed after latest developments allegedly pinpoint the location of the pseudonym, based on the timestamps of his/her posts.

According to “Cyberpunk” Jameson Lopp, CTO of CasaHodl, “Timestamps tell a story.” If the reported information is true, it would seem so and the curious case of Satoshi Nakamoto and Craig Wright can finally be put to bed.
DIVERGENCE BEGINS

Lopp charted both Satoshi Nakamoto and Craig S Wright’s hourly public activities over the 2009-2010 period, during which the “creator of Bitcoin” was active on a number of Bitcoin forums. If this evidence checks out, based on the variability of the two charts, Wright’s claim of being Satoshi Nakamoto can be heavily disputed.

Source: Twitter

Satoshi’s hourly activity is based on the “posts/code commits,” while Wright’s is based on “blog posts,” as per Lopp’s charts. Nakamoto’s location at the time was not revealed. However, Wright was residing in Australia at the time and hence, the time zones can be analyzed to present a clearer picture.

Given the variance of the hourly activity on the chart, Nakamoto’s fewest posts were between 0600 and 1300 UTC, while peak activity was recorded between 1600 and 2300 UTC. Wright’s chart showed less streamlined movement, with several spurts and dips. However, activity was relatively low between 1200 – 1900 UTC, with no blog posts between 1500-1700 UTC for the nChain chief scientist.
ASSUMPTION

On the assumption that the creator of Bitcoin hit the pillow between 2300 – 0100 and slept for a period of 6-7 hours, an inference can be made with respect to the charts.
TIME ZONES ANALYSED

Based on this assumption, if we consider Nakamoto to be based somewhere on the East Coast of the US [Eastern Time Zone, UTC-0500], a sleeping pattern of 0600 – 1300 would translate to the ETC time of 0100 – 0800, a fairly regular sleeping pattern. The West Coast of the United States can also be considered to be the location of the creator of Bitcoin. Based on the Pacific Time Zone, UTC-0800, the aforementioned sleeping pattern would be 2200 – 0500 PA. However, ETC time seems justifiable.

Since Wright was based in Australia, the time zone considered for the analysis is Australian Central Time [UTC + 0930]. When Lopp’s Nakamoto activity and Wright’s time zone are put together, the sleeping hours for the creator in Australian Time be 1530 – 2230, an irregular sleep cycle.

In light of this deviation, Lopp hypothesized that Nakamoto could be based in “eastern North America or western South America,” since the time zone coincides. His tweet read,

    “If you assume standard sleeping patterns then it appears Satoshi resided in eastern North America or western South America while Wright’s posts line up with eastern Australia.”

When considered in isolation, Wright’s chart solidifies Lopp’s claim. As mentioned above, Wright’s hourly activity dips between 1200 – 1700 UTC, which when converted to ACT, is 2130 – 0330, with no activity between 0130 – 0330. This corresponds to normal resting and sleeping patterns.
MOUNTING EVIDENCE

The variance between the public activities of the two is further exhibited by a set of charts posted by a Dr. Funkenstein, on the same thread. The handle claims the charts show “before and after” activities of Satoshi Nakamoto and Craig Wright, attesting to the above divergence.

Source: Twitter

Further, the aforementioned Twitter handle also posted public activity by the two from August 4, 2008 to November 1, 2011, showing a further difference. Based on the chart, Wright was very active towards the end of 2008, particularly November and December. Throughout 2009, his activity declined but was still more than Nakamoto’s.

The alleged creator only began picking the pace in October 2009, with consistent activity till the close of 2010. Nakamoto’s peak activity began only in May 2010, fading out by the close of the year. During this period, Wright was active only in late-August to early-September.

Source: Twitter

All the above charts, correlations, and variances indicate an alleged deviation between the activities of Satoshi Nakamoto and Craig Wright. Many in the community have already claimed that these charts will be the death knell to Wright’s claims of being Nakamoto.

The post Wright is Wrong: Timestamps indicate Satoshi Nakamoto’s location and refute CSW’s “claims” appeared first on AMBCrypto.
'''