"""
LDA Output:

(run 1 - Scikit-Learn online variational inference)

Topic 0:
loan fortescue slo_cashn oppose stand watch subsidy free meet talk
Topic 1:
tax pay public right destroy 10 slo_cash office loss opposition
Topic 2:
government australian look good know come way join coal ask
Topic 3:
future cut renewable wrong council policy question write lead set
Topic 4:
taxpayer price coal ½í² coalmine dollar local mega save massive
Topic 5:
reef coal green world barrier kill port leave end coral
Topic 6:
day wo industry huge run story miner mean solar worker
Topic 7:
½í turnbull power court coal ¼í pm start sell claim
Topic 8:
want fund time govt farmer bank ahead thank shorten state
Topic 9:
climate change coal say minister point beach face global political
Topic 10:
stop people think china disaster listen dam link dirty damage
Topic 11:
new need coal rail line election rule barnaby national joyce
Topic 12:
project action vote protest party coal cost high oil asset
Topic 13:
support energy win help community thing clean lie decision demand
Topic 14:
coal india tell fight indian try premier live billionaire hear
Topic 15:
job plan 000 news risk group coal create galilee ceo
Topic 16:
company slo_mention break build naif sign protect environment use native
Topic 17:
gas queensland money billion project narrabri lose iron ore seam
Topic 18:
labor lnp report federal approval alp land giant clear close
Topic 19:
water year work share environmental business deal make week buy



(run 1 - lda library  collapsed Gibbs sampling)

Topic 0: fund coal taxpayer loan bank money billion want govt dollar
Topic 1: thank time day action beach protest work people stop join
Topic 2: reef coal climate barrier stop future change need world destroy
Topic 3: gas water coal farmer project narrabri seam forest fine licence
Topic 4: job 000 create coal 10 lie thousand know time claim
Topic 5: coal company climate government australian board environmental face council ceo
Topic 6: court coal land approval native title people owner stop fight
Topic 7: rail loan line coal barnaby joyce fund queensland galilee basin
Topic 8: coal power india new energy renewable world clean solar need
Topic 9: labor green support vote stop shorten want alp lnp coal
Topic 10: tax ½í pay ½í² ¼í slo_cash company cut coal island
Topic 11: fortescue iron ore share price oil year fall dam profit


Time taken to process dataset: 696.9720530509949 seconds, 11.616200884183248 minutes, 0.19360334806972082 hours.


Process finished with exit code 0

###########################################################################################

(run 2 - Scikit-Learn LDA online variational inference)

Topic 0:
work court risk world group port native live title coal
Topic 1:
want good coalmine claim profit finance clear gov voter poll
Topic 2:
gas time coal know oppose thank industry narrabri think ask
Topic 3:
project fund reef climate coal change wo barrier kill watch
Topic 4:
fortescue protest cost local pm forest fine coal financial hand
Topic 5:
support fight right join wrong campaign demand planet country happen
Topic 6:
need farmer deal cut rule coal premier run royalty investment
Topic 7:
water australian future land question open coal pollution morning concern
Topic 8:
labor coal rail energy slo_cashn line win shorten election stop
Topic 9:
stop billion public action destroy dollar naif sign national party
Topic 10:
plan say business big council use end law year production
Topic 11:
new loan govt coal bank price giant make support long
Topic 12:
slo_mention tell help leave start environment talk massive away turn
Topic 13:
job government turnbull lnp look 000 year way lose create
Topic 14:
people queensland power let coal alp community thing stand close
Topic 15:
coal ½í build ½í² ¼í galilee ahead basin approve china
Topic 16:
company state iron indian ore news high lie face carbon
Topic 17:
tax pay break approval federal ceo subsidy issue slo_cash miner
Topic 18:
india money report come taxpayer point day barnaby joyce week
Topic 19:
green vote minister share sell canavan matt promise buy read



(run 2 - lda library collapsed Gibbs sampling)

Topic 0: tax ½í pay ½í² ¼í company slo_cash ¾í island corporate
Topic 1: gas coal water project narrabri seam point farmer plan forest
Topic 2: water court land farmer native coal title basin approval owner
Topic 3: coal climate future energy change world need new clean reef
Topic 4: loan coal rail fund line government queensland naif galilee labor
Topic 5: coal time thank late company india council australian minister board
Topic 6: fortescue iron ore barnaby joyce dam metal rail wa disaster
Topic 7: coal price share year oil asset power market high low
Topic 8: day action beach protest work join people stop win come
Topic 9: job reef coal 000 barrier create turnbull 10 cut lie
Topic 10: coal fund money bank taxpayer project want slo_cashn loan govt
Topic 11: labor green stop vote support shorten lnp alp want election


Time taken to process dataset: 696.3975586891174 seconds, 11.606625978151957 minutes, 0.19344376630253263 hours.


Process finished with exit code 0

"""

###########################################################################################

"""
HLDA Output:

TODO - run on Borg supercomputer as system RAM issue (out of memory).

(run 1)

....................................................................................................100
topic=0 level=0 (documents=653900): coal, $, job, 's, stop, project, want, í, tax, fund, 

....................................................................................................200
topic=0 level=0 (documents=653900): coal, $, job, 's, stop, project, want, í, tax, fund, 

....................................................................................................300
topic=0 level=0 (documents=653900): coal, $, job, 's, stop, project, want, í, tax, fund, 

....................................................................................................400
topic=0 level=0 (documents=653900): coal, $, job, 's, stop, project, want, í, tax, fund, 

....................................................................................................500
topic=0 level=0 (documents=653900): coal, $, job, 's, stop, project, want, í, tax, fund, 



Time taken to process dataset: 61687.211238861084 seconds, 1028.1201873143514 minutes, 17.13533645523919 hours.


Process finished with exit code 0

###########################################################################################

(run 2)
(below with recursive tree depth of 2 only)

Process finished with exit code 137 (interrupted by signal 9: SIGKILL)

- failed to produce any output whatsoever.

###########################################################################################

(run 3)
(below with recursive tree depth of 3 only)

Process finished with exit code 137 (interrupted by signal 9: SIGKILL)

- failed to produce any output whatsoever.

"""

###########################################################################################

"""
HDP Output:

(run 1)

(0, "0.025*coal + 0.008*job + 0.007*'s + 0.006*project + 0.006*stop + 0.006*want + 0.006*labor + 0.005*water + 0.005*fund + 0.005*loan")
(1, '0.082*í + 0.050*° + 0.043*tax + 0.041*½í² + 0.023*¼í¶\x93 + 0.016*pay + 0.013*$ + 0.012*coal + 0.010*energy + 0.008*½í')
(2, '0.170*$ + 0.009*cba + 0.009*anz + 0.009*wbc + 0.009*nab + 0.007*coal + 0.006*price + 0.005*fmg + 0.005*bxb + 0.005*syd')
(3, "0.016*coal + 0.005*'s + 0.005*job + 0.005*$ + 0.004*stop + 0.004*project + 0.004*want + 0.004*í + 0.003*fund + 0.003*reef")
(4, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*fund + 0.003*gas + 0.003*labor")
(5, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*gas + 0.003*water + 0.003*fund")
(6, "0.015*coal + 0.005*$ + 0.005*job + 0.005*'s + 0.004*stop + 0.004*project + 0.004*want + 0.003*gas + 0.003*fund + 0.003*support")
(7, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*gas + 0.003*fund + 0.003*labor")
(8, "0.015*coal + 0.005*job + 0.004*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.003*want + 0.003*gas + 0.003*fund + 0.003*support")
(9, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*water + 0.003*gas + 0.003*fund")
(10, "0.015*coal + 0.005*'s + 0.005*job + 0.004*$ + 0.004*stop + 0.004*project + 0.004*argyle + 0.004*want + 0.003*gas + 0.003*fund")
(11, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*í + 0.003*fund + 0.003*gas")
(12, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*want + 0.003*gas + 0.003*fund + 0.003*labor")
(13, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*gas + 0.003*fund + 0.003*water")
(14, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.004*fund + 0.003*gas + 0.003*labor")
(15, "0.015*coal + 0.005*job + 0.005*'s + 0.004*project + 0.004*stop + 0.004*$ + 0.004*want + 0.004*gas + 0.003*water + 0.003*fund")
(16, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*support + 0.003*gas")
(17, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*gas + 0.003*support")
(18, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*support + 0.003*labor")
(19, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*gas + 0.003*fund + 0.003*labor")


Time taken to process dataset: 1036.1106204986572 seconds, 17.268510341644287 minutes, 0.28780850569407146 hours.


Process finished with exit code 0

###########################################################################################

(run 2)

(0, "0.024*coal + 0.008*job + 0.007*'s + 0.006*want + 0.006*stop + 0.006*labor + 0.006*project + 0.005*fund + 0.005*support + 0.005*reef")
(1, '0.158*$ + 0.009*cba + 0.008*anz + 0.008*wbc + 0.008*nab + 0.007*coal + 0.007*price + 0.005*fmg + 0.005*share + 0.005*bxb')
(2, '0.086*í + 0.050*° + 0.043*½í² + 0.032*tax + 0.025*¼í¶\x93 + 0.015*$ + 0.013*coal + 0.009*energy + 0.007*½í + 0.006*pay')
(3, "0.020*coal + 0.013*gas + 0.008*water + 0.007*project + 0.005*'s + 0.005*seam + 0.004*narrabri + 0.004*new + 0.004*rail + 0.004*company")
(4, "0.035*tax + 0.024*pay + 0.012*coal + 0.007*'s + 0.006*ato + 0.005*energy + 0.004*job + 0.004*company + 0.004*haven + 0.004*chevron")
(5, '0.015*coal + 0.006*job + 0.006*go + 0.006*money + 0.006*taxpayer + 0.005*india + 0.005*joyce + 0.005*barnaby + 0.005*think + 0.005*give')
(6, "0.015*coal + 0.005*job + 0.005*'s + 0.004*project + 0.004*stop + 0.004*$ + 0.004*want + 0.003*fund + 0.003*gas + 0.003*reef")
(7, "0.016*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*loan + 0.004*fund + 0.004*want + 0.003*support")
(8, "0.015*coal + 0.005*job + 0.005*'s + 0.004*loan + 0.004*project + 0.004*stop + 0.004*labor + 0.004*$ + 0.004*want + 0.003*reef")
(9, "0.015*coal + 0.006*job + 0.006*council + 0.005*townsville + 0.005*'s + 0.004*$ + 0.004*project + 0.004*stop + 0.004*fund + 0.004*pay")
(10, "0.016*coal + 0.005*í + 0.005*'s + 0.005*job + 0.004*$ + 0.004*° + 0.004*stop + 0.004*project + 0.004*want + 0.003*labor")
(11, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*water + 0.003*tax + 0.003*gas")
(12, "0.016*coal + 0.005*job + 0.005*'s + 0.004*fund + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*water + 0.003*gas")
(13, "0.015*coal + 0.005*job + 0.004*'s + 0.004*stop + 0.004*$ + 0.004*project + 0.004*want + 0.003*water + 0.003*fund + 0.003*gas")
(14, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*í + 0.003*fund + 0.003*support")
(15, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*gas + 0.003*fund + 0.003*support")
(16, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*gas + 0.003*support")
(17, "0.015*coal + 0.006*í + 0.005*job + 0.004*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*gas")
(18, "0.015*coal + 0.006*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*gas + 0.003*support")
(19, "0.015*coal + 0.005*job + 0.005*'s + 0.004*$ + 0.004*stop + 0.004*project + 0.004*want + 0.003*fund + 0.003*labor + 0.003*gas")


Time taken to process dataset: 1036.3824276924133 seconds, 17.273040461540223 minutes, 0.2878840076923371 hours.


Process finished with exit code 0

"""

###########################################################################################

"""
Biterm Output:

(run 1)

 Topic coherence ..
Topic 0 | Coherence=-146.13 | Top words= coal stop labor want climate support project tax new shorten
Topic 1 | Coherence=-145.24 | Top words= support stop green labor people climate change queensland government oppose
Topic 2 | Coherence=-134.33 | Top words= rail line basin water galilee land support project farmer gas
Topic 3 | Coherence=-183.76 | Top words= coal iron ore fortescue year price climate people need stop
Topic 4 | Coherence=-147.70 | Top words= coal power energy price new india renewable solar year plant
Topic 5 | Coherence=-155.60 | Top words= coal job reef project barrier gas 000 create time stop
Topic 6 | Coherence=-156.48 | Top words= gas coal farmer project want people water govt pipeline tell
Topic 7 | Coherence=-157.07 | Top words= coal water queensland loan point fund new time year line
Topic 8 | Coherence=-166.53 | Top words= coal gas group people seam want plan water climate north
Topic 9 | Coherence=-155.40 | Top words= coal india power company stop need year indian plan report
Topic 10 | Coherence=-196.49 | Top words= tax pay title native company loan energy slo_cash government island
Topic 11 | Coherence=-152.78 | Top words= job coal court people 000 labor 10 time reef queensland
Topic 12 | Coherence=-132.85 | Top words= barnaby joyce gas coal project taxpayer money rail new india
Topic 13 | Coherence=-161.65 | Top words= job fund want project bank people work tell good public
Topic 14 | Coherence=-163.39 | Top words= coal new time need energy job project fund council thank
Topic 15 | Coherence=-134.58 | Top words= coal fund loan reef taxpayer want money slo_cashn stop govt
Topic 16 | Coherence=-149.31 | Top words= tax pay cut job govt australian billion turnbull dollar point
Topic 17 | Coherence=-138.75 | Top words= water support reef risk basin climate world right want artesian
Topic 18 | Coherence=-151.31 | Top words= coal labor loan want job billion dollar voter lnp turnbull
Topic 19 | Coherence=-128.80 | Top words= cut turnbull billion park push marine week litre groundwater big


 Texts & Topics ..
president national party lobby company represent    (topic: 14)
holy shit tho fortescue ascend literally famous price know (topic: 0)
good news muswellbrook hospital 's ed redevelopment donation    (topic: 13)
important film life depend    (topic: 0)
beef fork fork o pork    hahahahha omg í ½í¸í ½í¸í ½í¸slo_hash (topic: 16)
yes yes yes action protect collective future (topic: 0)
science teach professor laurie santosâ     > > yale happy course online free | think    (topic: 0)
exxon mobile chevron shell holding make billion aus resource pay zero tax think profitable 2 business despite corporate tax rate gleefully avoid duly reward aus economy automate job (topic: 16)
epa investigate discharge    (topic: 0)


Time taken to process dataset: 32306.65420603752 seconds, 538.4442367672921 minutes, 8.974070612788202 hours.

###########################################################################################

(run 2)

 Topic coherence ..
Topic 0 | Coherence=-151.18 | Top words= coal support job climate want world right reef risk company
Topic 1 | Coherence=-168.36 | Top words= water billion coal basin tax turnbull new fortescue government loan
Topic 2 | Coherence=-143.13 | Top words= tax company rail gas money stop australian coal line government
Topic 3 | Coherence=-138.24 | Top words= job 000 coal reef create project 10 want turnbull renewable
Topic 4 | Coherence=-141.34 | Top words= coal native title land court queensland stop government owner traditional
Topic 5 | Coherence=-138.89 | Top words= coal labor stop loan fund want project election rail shorten
Topic 6 | Coherence=-156.23 | Top words= coal green labor support people stop farmer vote oppose protest
Topic 7 | Coherence=-158.98 | Top words= coal new gas project india plan price government australian report
Topic 8 | Coherence=-182.12 | Top words= coal new australian loan gas power report good help minister
Topic 9 | Coherence=-152.07 | Top words= tax pay coal ½í energy year company ½í² origin ¼í
Topic 10 | Coherence=-160.66 | Top words= coal new point court reef project job australian labor approval
Topic 11 | Coherence=-195.12 | Top words= gas project water coal narrabri time seam farmer ore iron
Topic 12 | Coherence=-168.23 | Top words= job pay india money power council bank taxpayer build tax
Topic 13 | Coherence=-136.61 | Top words= coal reef climate barrier future energy people clean fund need
Topic 14 | Coherence=-151.80 | Top words= coal want time money fund loan canavan bank matt project
Topic 15 | Coherence=-164.49 | Top words= tax want pay joyce project fund barnaby people minister new
Topic 16 | Coherence=-132.85 | Top words= barnaby joyce india think money taxpayer rail spend come govt
Topic 17 | Coherence=-153.26 | Top words= coal loan water slo_cashn point government rail break port queensland
Topic 18 | Coherence=-138.77 | Top words= coal stop reef want fund climate need money labor public
Topic 19 | Coherence=-182.66 | Top words= fortescue group metal site year court prevent owner respect traditional


 Texts & Topics ..
footage release rubbish claim maules creek quiet library    (topic: 10)
mgt finally sell asset    wo far pay usslo_cash debt    $ sto    (topic: 16)
josh frydenburg dual citizenship hungary think (topic: 0)
permanent worker sack hail creek coal ​the cfmeu demand explanation 's dec    (topic: 10)
.slo_mention company risk help tell aecom company risk away       (topic: 1)
's climate bomb senselessness 's coal     (topic: 13)
reminder twice people work reef area tourism coal entire state queensland risk real job imaginary job       (topic: 0)
reef killer    (topic: 0)
canavan little desperate ahead crazy desperate make wonder promise í ¾í´    (topic: 14)


Time taken to process dataset: 31171.22075152397 seconds, 519.5203458587329 minutes, 8.65867243097888 hours.


Process finished with exit code 0

"""

###########################################################################################

"""
Author-Topic Output:

(run 1)

Label: 1
Words: leard go look maules work think well get have property 
Label: 2
Words: project road beach news win rd downer ceo 's peter 
Label: 3
Words: gas coal farmer seam water stop community people want protest 
Label: 4
Words: creek write 's wa coal | project company timor plan 
Label: 5
Words: gas coal forest petroleum tycoon energy price oil sale whc 
Label: 6
Words: tax joyce barnaby slo_cashil pay chevron liberal rail coal origin 
Label: 7
Words: narrabri water gas risk basin coal national artesian > farmer 
Label: 8
Words: í ° ½í² beach field ¼í¶ tour $ win home 
Label: 9
Words: eis land coal water inland go seam want appliance fracking 
Label: 10
Words: $ wpl sto video sire share field day gain result 


Time taken to process dataset: 9229.738131284714 seconds, 153.82896885474523 minutes, 2.5638161475790873 hours.


Process finished with exit code 0

###########################################################################################

(run 2)

Label: 1
Words: leard go look maules work think well get have property 
Label: 2
Words: project road beach news win rd downer ceo 's peter 
Label: 3
Words: gas coal farmer seam water stop community people want protest 
Label: 4
Words: creek write 's wa coal | project company timor plan 
Label: 5
Words: gas coal forest petroleum tycoon energy price oil sale whc 
Label: 6
Words: tax joyce barnaby slo_cashil pay chevron liberal rail coal origin 
Label: 7
Words: narrabri water gas risk basin coal national artesian > farmer 
Label: 8
Words: í ° ½í² beach field ¼í¶ tour $ win home 
Label: 9
Words: eis land coal water inland go seam want appliance fracking 
Label: 10
Words: $ wpl sto video sire share field day gain result 


Time taken to process dataset: 9202.727442502975 seconds, 153.37879070838292 minutes, 2.5563131784730486 hours.


Process finished with exit code 0

"""

###########################################################################################

"""
NMF Output:

(run 1)

Topics using NMF Frobenius norm:
Topic 0:
coal india build seam power world kill point mega port
Topic 1:
loan naif rail slo_cashn veto taxpayer line money billion dollar
Topic 2:
job 000 create 10 thousand tourism lie claim renewable cut
Topic 3:
tax pay haven slo_cash company year ato corporate chevron profit
Topic 4:
gas seam narrabri field plan pipeline barnaby forest export joyce
Topic 5:
stop land destroy vote people green culture win work native
Topic 6:
time thank late sentinel come dear conservative remind pl daily
Topic 7:
reef barrier kill save destroy coral trust protect fight bleach
Topic 8:
labor support green vote lnp shorten election alp oppose party
Topic 9:
½í ¼í beach ½í² ¼í¼ ¾í look slo_hash day think
Topic 10:
want people know billion dollar look mega govt future win
Topic 11:
climate change action policy risk future title native world fight
Topic 12:
project narrabri ahead shorten mega win bank halt announce finance
Topic 13:
need india thing destroy culture land know good planet federal
Topic 14:
government queensland australian turnbull federal court approval point plan cut
Topic 15:
iron ore fortescue price share year metal news group production
Topic 16:
water farmer unlimited basin free year land risk artesian licence
Topic 17:
new plan open london report ceo protest day point break
Topic 18:
fund bank public rule coalmine taxpayer govt wo westpac infrastructure
Topic 19:
slo_mention think company tell stand thousand good way thing risk

Topics using generalized Kullback-Leibler divergence:
Topic 0:
coal build away indian massive environment india mean minister power
Topic 1:
tell say turnbull way ask make question happen try issue
Topic 2:
job 000 10 create claim lie thousand tourism renewable pm
Topic 3:
australian company oil face govt financial use fail write set
Topic 4:
project gas narrabri land forest farmer seam sign community field
Topic 5:
stop tax pay profit million corporate haven office rate island
Topic 6:
time thank good come late stand start leave week long
Topic 7:
reef barrier fight help kill destroy risk protect let save
Topic 8:
labor support green vote lnp win election shorten alp party
Topic 9:
½í beach ¼í read love ½í² slo_hash letter oh ¾í
Topic 10:
want people know billion future dollar listen industry mega video
Topic 11:
day action protest court group right join wrong native meet
Topic 12:
climate change energy bank clean policy demand chief carbon fact
Topic 13:
need money look india deal thing barnaby loan joyce slo_cashn
Topic 14:
government news break report point ceo business cut giant cost
Topic 15:
year plan work world power dam big resource china large
Topic 16:
water queensland basin farmer approval ahead galilee environmental free licence
Topic 17:
new loan rail line taxpayer naif poll minister open veto
Topic 18:
fund govt coalmine federal wo state rule huge bank decision
Topic 19:
slo_mention fortescue price company think share iron ore high sell


Time taken to process dataset: 273.3467524051666 seconds, 4.555779206752777 minutes, 0.07592965344587961 hours.


Process finished with exit code 0

###########################################################################################

(run 2)

Topics using NMF Frobenius norm:
Topic 0:
coal india build seam power world kill point mega port
Topic 1:
loan naif rail slo_cashn veto taxpayer line money billion dollar
Topic 2:
job 000 create 10 thousand tourism lie claim renewable cut
Topic 3:
tax pay haven slo_cash company year ato corporate chevron profit
Topic 4:
gas seam narrabri field plan pipeline barnaby forest export joyce
Topic 5:
stop land destroy vote people green culture win work native
Topic 6:
time thank late sentinel come dear conservative remind pl daily
Topic 7:
reef barrier kill save destroy coral trust protect fight bleach
Topic 8:
labor support green vote lnp shorten election alp oppose party
Topic 9:
½í ¼í beach ½í² ¼í¼ ¾í look slo_hash day think
Topic 10:
want people know billion dollar look mega govt future win
Topic 11:
climate change action policy risk future title native world fight
Topic 12:
project narrabri ahead shorten mega win bank halt announce finance
Topic 13:
need india thing destroy culture land know good planet federal
Topic 14:
government queensland australian turnbull federal court approval point plan cut
Topic 15:
iron ore fortescue price share year metal news group production
Topic 16:
water farmer unlimited basin free year land risk artesian licence
Topic 17:
new plan open london report ceo protest day point break
Topic 18:
fund bank public rule coalmine taxpayer govt wo westpac infrastructure
Topic 19:
slo_mention think company tell stand thousand good way thing risk

Topics using generalized Kullback-Leibler divergence:
Topic 0:
coal build away indian massive minister india power mean solar
Topic 1:
tell turnbull say way ask happen question make try council
Topic 2:
job 000 10 create claim lie thousand tourism pm renewable
Topic 3:
australian company oil face govt write fail financial use set
Topic 4:
project gas narrabri land forest farmer sign seam field community
Topic 5:
stop tax pay profit million corporate haven office rate island
Topic 6:
time thank good come late stand start leave week end
Topic 7:
reef barrier fight help kill destroy risk protect save let
Topic 8:
labor support vote lnp win green election alp party shorten
Topic 9:
½í beach ½í² ¼í read love slo_hash ¾í letter oh
Topic 10:
want people know billion future dollar mega listen industry video
Topic 11:
day action protest right group court join wrong local native
Topic 12:
climate change energy bank clean policy demand chief carbon fuel
Topic 13:
need money look india deal barnaby thing joyce slo_cashn loan
Topic 14:
government news break report point ceo business cut close giant
Topic 15:
year plan work world power dam big china resource large
Topic 16:
water queensland basin farmer approval ahead environmental galilee free licence
Topic 17:
new loan rail line taxpayer naif minister poll open veto
Topic 18:
fund coalmine govt federal green wo rule state bank decision
Topic 19:
slo_mention fortescue price company think share iron ore high sell


Time taken to process dataset: 271.20036005973816 seconds, 4.520006000995636 minutes, 0.07533343334992727 hours.


Process finished with exit code 0

"""

###########################################################################################
