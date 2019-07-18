"""
LDA Output:

(run 1)
Topic 0: adani coal reef great point loan barrier abbot fund turnbull
Topic 1: adani council environmental india company townsville corruption question know need
Topic 2: santos woodside bhp whitehaven beach oil dam year day iluka
Topic 3: adani labor support qld election stop vote loan shorten want
Topic 4: adani coal stop court people whitehaven action protest native carmichael
Topic 5: santos gas nsw water pilliga project narrabri coal csg seam
Topic 6: adani coal carmichael fund bank project power india new australian
Topic 7: bhp rio tinto billiton fortescue iron ore price share cut
Topic 8: climate coal change australia future energy need clean time world
Topic 9: job adani 000 coal create canavan 10 matt think lie
Topic 10: tax ½í pay adani ½í² bhp ¼í company slo_cash australia
Topic 11: adani water coal basin qld galilee great queensland rail free


Time taken to process dataset: 757.5309031009674 seconds, 12.62551505168279 minutes, 0.21042525086137984 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
Topic 0: tax adani ½í pay ½í² ¼í billion slo_cash company coal
Topic 1: climate coal adani change future australia people stop reef need
Topic 2: whitehaven santos day beach action protest coal work join people
Topic 3: bhp rio tinto billiton fortescue iron ore share dam year
Topic 4: adani loan fund taxpayer money coal rail bank naif line
Topic 5: santos gas nsw water pilliga project narrabri coal csg seam
Topic 6: coal adani india power new carmichael fuel fossil energy solar
Topic 7: adani carmichael coal court approval coalmine native title stop land
Topic 8: adani coal great reef water barrier basin point abbot qld
Topic 9: bhp woodside santos oil australia company australian price gas ceo
Topic 10: job adani 000 create 10 coal lie qld late tourism
Topic 11: adani labor support stop vote shorten qld want lnp election


Time taken to process dataset: 757.9303824901581 seconds, 12.632173041502634 minutes, 0.21053621735837724 hours.


Process finished with exit code 0

"""

"""
HLDA Output:

TODO - run on Borg supercomputer as system RAM issue (out of memory).

(run 1)
(below with recursive tree depth of 1 only)

..................................................50
topic=0 level=0 (documents=654070): adani, coal, santos, bhp, $, 's, job, australia, rio, project, 

..................................................100
topic=0 level=0 (documents=654070): adani, coal, santos, bhp, $, 's, job, australia, rio, project, 



Time taken to process dataset: 13477.575538873672 seconds, 224.62625898122786 minutes, 3.743770983020464 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
(below with recursive tree depth of 2 only)

"""

"""
HDP Output:

(run 1)
(0, "0.044*adani + 0.022*coal + 0.008*santos + 0.007*job + 0.007*'s + 0.006*bhp + 0.006*project + 0.006*stop + 0.005*australia + 0.005*want")
(1, '0.076*í + 0.048*° + 0.042*tax + 0.040*½í² + 0.022*¼í¶\x93 + 0.021*adani + 0.016*pay + 0.013*$ + 0.011*coal + 0.010*energy')
(2, '0.144*$ + 0.027*bhp + 0.013*rio + 0.012*adani + 0.008*cba + 0.008*anz + 0.007*wbc + 0.007*nab + 0.006*coal + 0.006*price')
(3, "0.028*adani + 0.013*coal + 0.009*santos + 0.007*bhp + 0.006*rio + 0.005*australia + 0.005*tinto + 0.004*'s + 0.004*job + 0.004*$")
(4, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*job + 0.004*'s + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*stop")
(5, "0.029*adani + 0.014*coal + 0.009*santos + 0.007*bhp + 0.004*australia + 0.004*'s + 0.004*job + 0.004*rio + 0.004*project + 0.004*$")
(6, "0.026*adani + 0.013*coal + 0.011*bhp + 0.007*santos + 0.007*rio + 0.006*tinto + 0.004*$ + 0.004*australia + 0.004*job + 0.004*'s")
(7, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*stop + 0.004*rio + 0.004*$")
(8, "0.028*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.004*rio + 0.004*'s + 0.004*australia + 0.004*job + 0.004*$ + 0.004*project")
(9, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*stop")
(10, "0.029*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.004*$ + 0.004*'s + 0.004*rio + 0.004*australia + 0.004*job + 0.004*project")
(11, "0.029*adani + 0.014*coal + 0.009*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*stop + 0.004*project")
(12, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*project")
(13, "0.029*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.004*rio + 0.004*'s + 0.004*australia + 0.004*job + 0.004*$ + 0.004*project")
(14, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*australia + 0.004*job + 0.004*rio + 0.004*$ + 0.004*project")
(15, "0.028*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.007*$ + 0.005*í + 0.004*rio + 0.004*australia + 0.004*job + 0.004*'s")
(16, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*$ + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*project")
(17, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*project")
(18, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*stop")
(19, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.005*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*project")


Time taken to process dataset: 1077.2826988697052 seconds, 17.95471164782842 minutes, 0.2992451941304737 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
(0, "0.046*adani + 0.022*coal + 0.008*job + 0.007*bhp + 0.007*'s + 0.006*project + 0.006*stop + 0.006*santos + 0.005*australia + 0.005*want")
(1, '0.079*í + 0.048*° + 0.040*tax + 0.040*½í² + 0.022*¼í¶\x93 + 0.021*adani + 0.016*pay + 0.013*$ + 0.011*coal + 0.009*energy')
(2, '0.030*santos + 0.019*adani + 0.016*gas + 0.013*coal + 0.012*nsw + 0.011*water + 0.008*pilliga + 0.007*great + 0.006*project + 0.006*narrabri')
(3, '0.154*$ + 0.024*bhp + 0.014*adani + 0.010*rio + 0.008*cba + 0.008*wbc + 0.008*anz + 0.008*nab + 0.007*coal + 0.005*price')
(4, "0.030*adani + 0.017*coal + 0.008*santos + 0.007*bhp + 0.005*'s + 0.004*australia + 0.004*rio + 0.004*job + 0.004*project + 0.003*want")
(5, "0.029*adani + 0.016*coal + 0.010*santos + 0.007*bhp + 0.005*water + 0.005*gas + 0.004*'s + 0.004*point + 0.004*australia + 0.004*rio")
(6, "0.027*adani + 0.013*coal + 0.010*santos + 0.007*bhp + 0.006*'s + 0.004*project + 0.004*australia + 0.004*rio + 0.004*job + 0.004*$")
(7, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*stop")
(8, "0.026*adani + 0.013*coal + 0.010*bhp + 0.009*rio + 0.007*santos + 0.007*tinto + 0.005*australia + 0.004*$ + 0.004*'s + 0.004*job")
(9, "0.028*adani + 0.015*coal + 0.008*santos + 0.007*bhp + 0.004*job + 0.004*'s + 0.004*australia + 0.004*$ + 0.004*rio + 0.004*project")
(10, "0.029*adani + 0.013*coal + 0.008*santos + 0.007*bhp + 0.005*rio + 0.005*want + 0.004*'s + 0.004*job + 0.004*australia + 0.004*$")
(11, "0.028*adani + 0.014*coal + 0.009*santos + 0.007*bhp + 0.004*'s + 0.004*australia + 0.004*job + 0.004*$ + 0.004*rio + 0.004*stop")
(12, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*job + 0.004*$ + 0.004*'s + 0.004*australia + 0.004*rio + 0.004*project")
(13, "0.030*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*australia + 0.004*job + 0.004*rio + 0.004*$ + 0.004*stop")
(14, "0.029*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.004*job + 0.004*australia + 0.004*'s + 0.004*rio + 0.004*$ + 0.004*stop")
(15, "0.028*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*australia + 0.004*job + 0.004*rio + 0.004*$ + 0.003*stop")
(16, "0.029*adani + 0.014*coal + 0.008*santos + 0.008*bhp + 0.004*australia + 0.004*'s + 0.004*job + 0.004*$ + 0.004*rio + 0.004*project")
(17, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*australia + 0.004*job + 0.004*rio + 0.004*$ + 0.004*project")
(18, "0.029*adani + 0.014*coal + 0.009*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*stop")
(19, "0.029*adani + 0.014*coal + 0.008*santos + 0.007*bhp + 0.004*'s + 0.004*job + 0.004*australia + 0.004*rio + 0.004*$ + 0.004*project")


Time taken to process dataset: 1071.8396093845367 seconds, 17.863993489742278 minutes, 0.29773322482903797 hours.


Process finished with exit code 0

"""

"""
Biterm Output: (subset of all output)

(not the topics - just example of Tweets with assigned topics )
 world record objection 276 submission prepare submit invasive gas field    (topic: 13)
accenture join bhp set 50/50 gender target    (topic: 12)
colin barnett wrong iron ore bhp boss    (topic: 6)
approval adani queensland coalmine face legal challenge    hint (topic: 11)
declare buy 5 large parcel land 15 minute drive plan route        (topic: 18)
having whale time fortescue bay pic ig    (topic: 6)
question greens want govern australia greens voter support lnp continual attack australian defend attack labor lnp (topic: 17)
courage tear adani 's license people australia new legal advice show adani wo n’t able damn thing    (topic: 11)
's critical adani need controversial government loan    (topic: 0)
money matters 10 thing need know open bell spy spx qqq dia jpm aapl    (topic: 0)
right alp reconsider support adani    24 hour convince reject    email labor cabinet tell > >    (topic: 11)
annastacia palaszczuk billion dollar handout billionaire adani sign petition    (topic: 15)
dr nahan payroll tax hike tax job large employer coles woolies rio tinto etc (topic: 12)
matt canavan delusional think seq (topic: 0)
great silence single weatherill minister available talk listener bhp job hit (topic: 0)
australia 's climate bomb senselessness adani carmichael coal    (topic: 4)
listen local farmer tourism operator want protect land water coral    (topic: 17)


Time taken to process dataset: 39906.75524163246 seconds, 665.112587360541 minutes, 11.08520978934235 hours.


Process finished with exit code 0

###########################################################################################

(run 1)
Placeholder.

###########################################################################################

(run 2)
Placeholder.

"""

"""
Author-Topic Output:

(run 1)
Label: 1
Words: project written woodside santos eis north downer group coal .slo_mention 
Label: 2
Words: tax joyce barnaby inland woodside slo_cashil pay property chevron go 
Label: 3
Words: gas coal seam water rd stop farmer people time pipeline 
Label: 4
Words: woodside coal new 's energy | coleman wa project cfs 
Label: 5
Words: santos nsw gas great australia water narrabri pilliga basin pipeline 
Label: 6
Words: beach road win 1 tour day > video morning park 
Label: 7
Words: santos route have party breed be right well v like 
Label: 8
Words: woodside whitehaven lng coal tycoon rio oil price gas sale 
Label: 9
Words: í whitehaven $ ° ½í² ¼í¶ sto james whc ltd 
Label: 10
Words: santos forest coal gas narrabri water petroleum csg creek field 


Time taken to process dataset: 9772.976831436157 seconds, 162.8829471906026 minutes, 2.7147157865100433 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
Label: 1
Words: project written woodside santos eis north downer group coal .slo_mention 
Label: 2
Words: tax joyce barnaby inland woodside slo_cashil pay property chevron go 
Label: 3
Words: gas coal seam water rd stop farmer people time pipeline 
Label: 4
Words: woodside coal new 's energy | coleman wa project cfs 
Label: 5
Words: santos nsw gas great australia water narrabri pilliga basin pipeline 
Label: 6
Words: beach road win 1 tour day > video morning park 
Label: 7
Words: santos route have party breed be right well v like 
Label: 8
Words: woodside whitehaven lng coal tycoon rio oil price gas sale 
Label: 9
Words: í whitehaven $ ° ½í² ¼í¶ sto james whc ltd 
Label: 10
Words: santos forest coal gas narrabri water petroleum csg creek field 


Time taken to process dataset: 9236.188854932785 seconds, 153.9364809155464 minutes, 2.565608015259107 hours.


Process finished with exit code 0

"""

"""
NMF Output:

(run 1)
Topics using NMF Frobenius norm:
Topic 0:
adani turnbull india queensland ahead oppose indian water deal point
Topic 1:
rio tinto iron ore bulga new expansion uk sell london
Topic 2:
santos pilliga csg tour dos los narrabri plan home forest
Topic 3:
bhp billiton iron ore dam price brazil share cut australian
Topic 4:
coal new india power build price seam world kill point
Topic 5:
job 000 create 10 tourism thousand lie qld renewable energy
Topic 6:
reef great barrier artesian basin kill save destroy trust coral
Topic 7:
stop land destroy people culture vote native greens title win
Topic 8:
australia world future wake big large risk energy india thing
Topic 9:
carmichael need coalmine federal court approval land report culture queensland
Topic 10:
tax pay year slo_cash haven company fortescue ato corporate profit
Topic 11:
whitehaven beach creek maules forest day photo island protest clear
Topic 12:
project narrabri mega shorten bank ahead csg halt announce rt
Topic 13:
½í ¼í ½í² ¼í¼ ¾í slo_mention slo_hash ½í¹ think slo_cash
Topic 14:
gas nsw water seam narrabri field farmer pilliga pipeline land
Topic 15:
climate change time action policy risk future new slo_mention join
Topic 16:
want australian people know billion dollar future listen mega govt
Topic 17:
fund loan government taxpayer rail money naif public line bank
Topic 18:
woodside petroleum road oil lng price downer news search energy
Topic 19:
labor support qld vote lnp greens election shorten alp party

Topics using generalized Kullback-Leibler divergence:
Topic 0:
adani loan government minister turnbull india canavan face ahead question
Topic 1:
rio tinto iron ore bhp business close new mining fall
Topic 2:
santos gas nsw pilliga narrabri csg barnaby forest farmer water
Topic 3:
bhp billiton ceo dam disaster loss cut brazil boss asx
Topic 4:
coal new india build power open port dirty solar giant
Topic 5:
job 000 destroy create 10 lie real pm tourism claim
Topic 6:
great reef barrier help fight right world join kill basin
Topic 7:
stop labor election lnp vote greens win alp qld shorten
Topic 8:
australia energy future big clean industry thing demand planet fossil
Topic 9:
adani carmichael court coalmine approval land native challenge title owner
Topic 10:
pay tax company money billion cut dollar indian million billionaire
Topic 11:
whitehaven day beach protest anti iluka thank stand morning brisbane
Topic 12:
project ½í breaking finance decision china bank board ¼í wo
Topic 13:
support good party leave carbon policy issue huge fact mean
Topic 14:
fortescue environmental group galilee basin price away cost record happen
Topic 15:
people time slo_mention action come look work think power live
Topic 16:
want need know ahead let mega tell people listen govt
Topic 17:
fund climate change bank public federal report risk taxpayer money
Topic 18:
australian woodside news late oil thanks share video times sentinel
Topic 19:
qld water queensland govt government year point build deal line


Time taken to process dataset: 306.614928483963 seconds, 5.11024880806605 minutes, 0.0851708134677675 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
Topics using NMF Frobenius norm:
Topic 0:
adani turnbull india queensland ahead oppose indian water deal point
Topic 1:
rio tinto iron ore bulga new expansion uk sell london
Topic 2:
santos pilliga csg tour dos los narrabri plan home forest
Topic 3:
bhp billiton iron ore dam price brazil share cut australian
Topic 4:
coal new india power build price seam world kill point
Topic 5:
job 000 create 10 tourism thousand lie qld renewable energy
Topic 6:
reef great barrier artesian basin kill save destroy trust coral
Topic 7:
stop land destroy people culture vote native greens title win
Topic 8:
australia world future wake big large risk energy india thing
Topic 9:
carmichael need coalmine federal court approval land report culture queensland
Topic 10:
tax pay year slo_cash haven company fortescue ato corporate profit
Topic 11:
whitehaven beach creek maules forest day photo island protest clear
Topic 12:
project narrabri mega shorten bank ahead csg halt announce rt
Topic 13:
½í ¼í ½í² ¼í¼ ¾í slo_mention slo_hash ½í¹ think slo_cash
Topic 14:
gas nsw water seam narrabri field farmer pilliga pipeline land
Topic 15:
climate change time action policy risk future new slo_mention join
Topic 16:
want australian people know billion dollar future listen mega govt
Topic 17:
fund loan government taxpayer rail money naif public line bank
Topic 18:
woodside petroleum road oil lng price downer news search energy
Topic 19:
labor support qld vote lnp greens election shorten alp party

Topics using generalized Kullback-Leibler divergence:
Topic 0:
adani loan minister turnbull government canavan india face ahead corruption
Topic 1:
rio tinto iron ore business bhp new close fall miner
Topic 2:
santos gas nsw pilliga narrabri csg barnaby forest farmer water
Topic 3:
bhp billiton ceo dam disaster loss brazil cut asx boss
Topic 4:
coal new india build power port dirty solar import plan
Topic 5:
job 000 destroy create 10 lie tourism real pm thousand
Topic 6:
great reef barrier help fight right join world kill basin
Topic 7:
stop labor election lnp vote greens win alp shorten qld
Topic 8:
australia energy future big clean industry demand thing planet country
Topic 9:
adani carmichael court coalmine approval land title native report challenge
Topic 10:
pay tax company money billion cut dollar million indian billionaire
Topic 11:
whitehaven day beach protest anti iluka stand thank morning creek
Topic 12:
project ½í breaking finance decision china board investment slo_hash ¼í
Topic 13:
support good party leave carbon issue policy huge mean fact
Topic 14:
fortescue environmental group galilee basin cost away price record happen
Topic 15:
people time slo_mention action come look work think power live
Topic 16:
want need know ahead let tell mega govt community listen
Topic 17:
fund climate change bank public federal report risk government taxpayer
Topic 18:
australian woodside news late oil thanks share home times sentinel
Topic 19:
qld water queensland govt government year deal point build line


Time taken to process dataset: 323.3131334781647 seconds, 5.3885522246360775 minutes, 0.08980920374393463 hours.


Process finished with exit code 0

"""