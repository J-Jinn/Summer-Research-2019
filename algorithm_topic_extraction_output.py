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

..................................................50
topic=0 level=0 (documents=654070): adani, coal, 's, australia, want, stop, project, support, australian, new, 
    topic=1 level=1 (documents=13396): tax, í, pay, °, ½í², bhp, ¼í¶, ato, energy, rio, 
    topic=2 level=1 (documents=12084): climate, coal, reef, energy, emission, renewable, change, future, mine, water, 
    topic=3 level=1 (documents=12599): adani, water, unlimited, abbot, point, give, qld, farmer, free, government, 
    topic=4 level=1 (documents=17404): labor, greens, vote, adani, lnp, alp, qld, support, election, shorten, 
    topic=5 level=1 (documents=14819): adani, job, billion, taxpayer, dollar, turnbull, fund, public, $, pm, 
    topic=6 level=1 (documents=12483): santos, great, barnaby, water, joyce, basin, artesian, rail, gas, nsw, 
    topic=7 level=1 (documents=12840): $, bhp, rio, tinto, asx, price, fmg, cba, share, fall, 
    topic=8 level=1 (documents=15797): bhp, rio, tinto, iron, ore, billiton, dam, brazil, tax, disaster, 
    topic=9 level=1 (documents=7478): rio, late, thanks, tinto, times, sentinel, share, bhp, nico, topic, 
    topic=10 level=1 (documents=9896): santos, woodside, tour, win, stage, road, í, rd, written, tycoon, 
    topic=11 level=1 (documents=16507): santos, gas, pilliga, nsw, water, seam, forest, csg, narrabri, farmer, 
    topic=12 level=1 (documents=13764): woodside, santos, gas, oil, lng, search, price, $, petroleum, browse, 
    topic=13 level=1 (documents=4269): santos, president, bonacci, colombia, party, video, national, peace, 1, donor, 
    topic=14 level=1 (documents=8099): protest, watch, anti, melbourne, law, monday, roadshow, tonight, digging, outside, 
    topic=15 level=1 (documents=1190): close, euro, prices, rio.uk, bhp.uk, relationship, reveal, documents, cosy, baird, 
    topic=16 level=1 (documents=6323): water, santos, gas, pilliga, creek, whitehaven, narrabri, werris, farmer, seam, 
    topic=17 level=1 (documents=4500): santos, aquifer, fine, contaminate, financial, slo_cash0, uranium, csg, water, project, 
    topic=18 level=1 (documents=3474): grazier, queensland, farmer, vote, currie, fight, coral, farmers, bruce, environmental, 
    topic=19 level=1 (documents=8220): bhp, tinto, rio, billiton, wa, scandal, newmont, olympic, contract, |, 
    topic=20 level=1 (documents=2647): black, folk, clive, count, medium, lung, roberts, monster, palmer, malcolm, 
    topic=21 level=1 (documents=9793): clean, future, energy, demand, australia, climate, child, job, planet, n’t, 
    topic=22 level=1 (documents=3632): woodside, na, gon, polly, build, cheese, centre, art, sa, wrights, 
    topic=23 level=1 (documents=3837): iluka, beach, resources, nsw, woodside, group, bay, whitehaven, shark, santos, 
    topic=24 level=1 (documents=4998): accept, respect, prevent, protester, anti, sydney, premier, outside, election, whitehaven, 
    topic=25 level=1 (documents=5330): santos, pipeline, farmer, nsw, break, coonamble, lock, police, gas, senator, 
    topic=26 level=1 (documents=5452): canavan, matt, ian, adani, donation, labor, chappell, federal, coalition, minister, 
    topic=27 level=1 (documents=4664): stack, environmentally, shorten, adani, economically, viable, >, fund, govt, n’t, 
    topic=28 level=1 (documents=9127): coal, power, india, adani, carmichael, import, solar, climate, hunt, greg, 
    topic=29 level=1 (documents=6545): townsville, council, carmichael, letter, airstrip, money, carbon, airport, í, ratepayer, 
    topic=30 level=1 (documents=4984): question, adani, answer, think, digging, ask, turnbull, website, program, decline, 
    topic=31 level=1 (documents=3155): fossil, fuel, c, °, global, warm, temperature, rise, admit, company, 
    topic=32 level=1 (documents=1531): past, shonky, 's, dirty, boom, woodside, miss, +, land, behaviour, 
    topic=33 level=1 (documents=7116): whitehaven, coal, maules, forest, creek, leard, clear, state, stop, nsw, 
    topic=34 level=1 (documents=3542): ceo, disaster, record, pollution, track, disclose, adani, african, boss, environmental, 
    topic=35 level=1 (documents=13508): adani, native, title, court, traditional, land, carmichael, owner, federal, wangan, 
    topic=36 level=1 (documents=7532): tax, haven, cayman, adani, islands, company, money, taxpayer, pay, shift, 
    topic=37 level=1 (documents=4068): joyce, barnaby, adani, india, wed, direct, fund, pay, twitter, action, 
    topic=38 level=1 (documents=11225): reef, barrier, great, í, coral, adani, save, destroy, trust, protect, 
    topic=39 level=1 (documents=7438): point, abbot, coal, fine, adani, port, terminal, breach, water, sediment, 
    topic=40 level=1 (documents=2990): message, billion, dollar, simple, clear, send, bye, be, get, handout, 
    topic=41 level=1 (documents=5125): beach, whitehaven, í, whitsundays, island, sand, whitsunday, beautiful, day, ig, 
    topic=42 level=1 (documents=13560): bhp, billiton, $, mackenzie, dividend, andrew, loss, cut, ceo, price, 
    topic=43 level=1 (documents=11077): adani, royalty, money, loan, qld, taxpayer, deal, holiday, slo_cashn, turnbull, 
    topic=44 level=1 (documents=4741): water, adani, groundwater, finch, farmer, world, licence, 's, approval, plan, 
    topic=45 level=1 (documents=9521): bank, adani, fund, rule, carmichael, coalmine, westpac, china, project, finance, 
    topic=46 level=1 (documents=5050): action, day, join, big, beach, rally, cairns, brisbane, people, melbourne, 
    topic=47 level=1 (documents=3760): santos, dos, junior, ufc, vs, fight, vs., matthew, play, neymar, 
    topic=48 level=1 (documents=6221): office, arrest, occupy, protest, hq, breaking, leader, blockade, climate, outside, 
    topic=49 level=1 (documents=1249): crony, capitalism, include, carmichael, row, pollies, journalist, proposal, strand, fail, 
    topic=50 level=1 (documents=5052): adani, loan, point, abbot, report, coal, poll, wetland, voter, spill, 
    topic=51 level=1 (documents=2594): barnaby, joyce, way, go, wrong, game, dirty, breaking, unbankable, exposing, 
    topic=52 level=1 (documents=1528): finance, bank, insider, china, 17, knock, australian, cost, job, think, 
    topic=53 level=1 (documents=2224): wind, price, coal, solar, new, latest, project, tender, half, recover, 
    topic=54 level=1 (documents=710): cost, aside, í, culture, dot, scientist, popular, investment, environment, outrage, 
    topic=55 level=1 (documents=2850): santos, high, eis, quality, low, ash, water, india, groundwater, expert, 
    topic=56 level=1 (documents=3935): woodside, ceo, bhp, board, peter, santos, coleman, executive, billiton, chairman, 
    topic=57 level=1 (documents=632): ben, christensen, george, threat, pennings, death, baby, jerry, mid, cut, 
    topic=58 level=1 (documents=1231): native, title, law, shame, change, back, promised, sound, thank, like, 
    topic=59 level=1 (documents=1140): kevin, santos, gallagher, gas, ceo, humphries, door, burning, mp, answer, 
    topic=60 level=1 (documents=1261): icac, birthday, federal, 200th, party, bday, questionable, protester, happy, anti, 
    topic=61 level=1 (documents=594): kills, knox, 17, trillion, pizza, numbers, 9, april, property, santos, 
    topic=62 level=1 (documents=1608): subsidise, rail, feds, townsville, mayor, turnbull, report, job, council, argument, 
    topic=63 level=1 (documents=1784): jobs, create, 10,000, claims, john, tourism, leave, railway, bonanza, quiggin, 
    topic=64 level=1 (documents=837): alp, cheer, story, squad, record, fierce, track, detention, concerns, mount, 
    topic=65 level=1 (documents=1503): bollard, renewable, people, employ, melbourne, govt, qld, push, 7, cefc, 
    topic=66 level=1 (documents=7848): santos, gas, narrabri, nsw, project, eis, submission, seam, objection, field, 
    topic=67 level=1 (documents=2033): new, mine, coal, duty, civic, shameful, open, abandon, day, justify, 
    topic=68 level=1 (documents=2713): fraud, loan, call, financial, adani, australian, face, getup, giant, claim, 
    topic=69 level=1 (documents=334): gunns, tax, mill, folly, interesting, power, champion, pulp, payer, wilful, 
    topic=70 level=1 (documents=3422): rio, tinto, truck, job, driverless, automate, ore, iron, autonomous, port, 
    topic=71 level=1 (documents=917): import, india, petition, sign, game, un, vs, indian, usslo_cash, urgent, 
    topic=72 level=1 (documents=661): shut, museum, edition, santos, economic, party, botany, shot, exports, dancers, 
    topic=73 level=1 (documents=1594): abbott, tony, stupid, santos, divest, anu, call, decision, sabotage, comment, 
    topic=74 level=1 (documents=617): swim, tide, westpac, pool, decision, silent, alliance, yr, attack, swallow, 
    topic=75 level=1 (documents=1764): batman, election, ad, honest, campaign, turnbull, trump, rupert, mining, problem, 
    topic=76 level=1 (documents=4603): galilee, basin, rail, gina, rinehart, line, project, mine, adani, coal, 
    topic=77 level=1 (documents=1295): frydenberg, josh, nsw, ho, hey, eye, happen, roberts, project, distress, 
    topic=78 level=1 (documents=1143): challenge, loan, fiona, asylum, seeker, high, refugee, manus, court, ripe, 
    topic=79 level=1 (documents=333): abad, fire, integrity, myth, city, enterprises, manila, debt, general, currently, 
    topic=80 level=1 (documents=751): steel, arrium, whyalla, public, rail, solar, order, railway, lifeline, tonne, 
    topic=81 level=1 (documents=844): cairns, port, douglas, vote, survey, church, coral, 98, strong, message, 
    topic=82 level=1 (documents=245): files, afford, wrong, hundreds, costs, kwh, digital, hidden, running, sordid, 
    topic=83 level=1 (documents=5851): climate, change, sea, warm, global, rise, ocean, level, planet, |, 
    topic=84 level=1 (documents=484): coral, forever, charles, ditch, prince, veron, charlie, urge, risk, evil, 
    topic=85 level=1 (documents=1791): asset, jones, alan, sell, pressure, strand, agree, hanson, pauline, debt, 
    topic=86 level=1 (documents=438): u, legally, slo_cashb, questionable, q, toss, tho, a+, minister, charge, 
    topic=87 level=1 (documents=707): battery, musk, elon, void, backs, deep, scientists, expose, screams, tesla, 
    topic=88 level=1 (documents=208): reputation, band, urge, tarnish, ¾í´£, competitor, miner, well, í, btwn, 
    topic=89 level=1 (documents=2965): bob, brown, franklin, launch, adani, alliance, stop, people, river, oppose, 
    topic=90 level=1 (documents=12348): rio, tinto, bulga, $, expansion, sell, hunter, fraud, billion, warkworth, 
    topic=91 level=1 (documents=1399): canavan, matt, lie, station, citizenship, westpac, story, power, deny, minister, 
    topic=92 level=1 (documents=10311): job, create, 10,000, adani, thousand, lie, tourism, court, reef, ten, 
    topic=93 level=1 (documents=422): process, wa, mention, susceptible, approval, corruption.slo_hash, show, replace, lawyer, report, 
    topic=94 level=1 (documents=4515): í, °, ½í, ½í±, ½í¸, ½í±í, ©, ¼í, ½í¸¡í, ½í², 
    topic=95 level=1 (documents=477): true, railway, myths, shut, tree, attach, diane, blast, hart, natalie, 
    topic=96 level=1 (documents=1400): oil, secret, andrew, midnight, spill, robb, keep, chinese, exclusive, dangerous, 
    topic=97 level=1 (documents=433): idiot, bloody, royalty, profit, conglomerate, usually, gun, taxis, stupid, premier, 
    topic=98 level=1 (documents=952): al, et, tim, gore, nut, power, provide, net, buckley, hockey, 
    topic=99 level=1 (documents=425): penny, wong, jenny, wine, dine, csg, trough, snout, outrageous, macklin, 
    topic=100 level=1 (documents=613): reason, truly, westpac, subsidy, lavish, crack, seven, idea, conviction, quolls, 
    topic=101 level=1 (documents=569): care, aged, lnp, cut, gift, gbr, ruin, die, hsbc, plug, 
    topic=102 level=1 (documents=282): bishop, leo, follow, clinton, feed, ash, uk, humiliate, abbott, suit, 
    topic=103 level=1 (documents=648): milner, cameron, lobbyist, limb, wld, sticker, boy, campaign, subsidy, conflict, 
    topic=104 level=1 (documents=350): jesus, flip, origin, slo_cashb, finish, christ, klein, 55, bungle, commonwealth, 
    topic=105 level=1 (documents=441): hill, broken, mayor, paul, messy, palaszczuk, choice, nuclear, csg, option, 
    topic=106 level=1 (documents=1239): mega, abbott, propose, activist, increasingly, infiltrate, law, sue, vigilante, threaten, 
    topic=107 level=1 (documents=14336): loan, adani, naif, veto, rail, fund, line, board, government, qld, 
    topic=108 level=1 (documents=521): c, average, madness, l, normal, temp, utter, co., r, focus, 
    topic=109 level=1 (documents=546): cleanup, subsidise, enter, bucket, oã¥o, brush, exception, assume, corruption, parrot, 
    topic=110 level=1 (documents=2313): indian, investigation, poverty, india, political, influence, power, donation, lift, price, 
    topic=111 level=1 (documents=422): angry, forget, ohh, farmers, start, special, impact, deal, lnp, ping, 
    topic=112 level=1 (documents=1076): home, help, love, town, treat, buyer, wollongong, buyers, be, wonder, 
    topic=113 level=1 (documents=280): closing, prime, coral, window, 37, don't, reefs, sites, largest, rapidly, 
    topic=114 level=1 (documents=323): lack, press, clearly, institution, pole, fairfax, substance, germany, note, murdoch, 
    topic=115 level=1 (documents=894): price, pollution, v, pay, carbon, brandis, dad, bhp, mum, abbott, 
    topic=116 level=1 (documents=244): shovel, farming, faction, husband, psychic, misses, fixing, vine, banker, feud, 
    topic=117 level=1 (documents=311): realistic, threaten, policy, stack, environmentally, security, think, btw, national, promote, 
    topic=118 level=1 (documents=1359): york, new, bhp, rio, london, times, thing, need, planet, editorial, 
    topic=119 level=1 (documents=349): property, practise, farmer, consultant, sanction, ecological, trespass, guy, certify, bulldozer, 
    topic=120 level=1 (documents=1184): í, ¾í´£í, ½í¸í, ½í¸, ¾í´£, derail, ½í²ª, zilch, nada, ½í¸, 
    topic=121 level=1 (documents=514): democracy, politician, freedom, contempt, penguin, sear, explain, approval, reveal, parent, 
    topic=122 level=1 (documents=723): pacific, islanders, coalmine, fund, australia, fate, downer, greed, way, seal, 
    topic=123 level=1 (documents=985): bhp, gender, woman, diversity, experience, insane, workforce, mackenzie, billiton, andrew, 
    topic=124 level=1 (documents=681): marriage, audience, postal, survey, equality, shd, plebiscite, abt, reckon, subsidise, 
    topic=125 level=1 (documents=530): wall, directly, stick, demise, delight, relate, flowchart, malcolm, point, .slo_mention, 
    topic=126 level=1 (documents=241): colin, barnett, dr, equivocate, cancer, nurse, breast, union, glen, forklift, 
    topic=127 level=1 (documents=363): adrian, retention, photo, datum, asylum, burragubba, id, seeker, siamese, wgarcompilation, 
    topic=128 level=1 (documents=1248): debt, india, gautam, crore, port, modi, farmer, power, rs, scam, 
    topic=129 level=1 (documents=226): location, kilometre, baseline, square, viral, furious, pac, nearby, bylong, spray, 
    topic=130 level=1 (documents=304): warm, soup, life, seawater, wade, near, 16, big, fascinating, record, 
    topic=131 level=1 (documents=451): means, footy, business, nt, fracking, program, resolution, unanimous, mcarthur, basin, 
    topic=132 level=1 (documents=432): ©, responsible, red, ill, carpet, special, tonight, ¾í´, cis, prã, 
    topic=133 level=1 (documents=787): santos, ann, judy, vilma, dos, stars, star, angel, concert, mp, 
    topic=134 level=1 (documents=5573): shorten, bill, labor, adani, announce, project, election, stop, mega, win, 
    topic=135 level=1 (documents=321): matilda, series, special, introduction, burke, malcolm, return, spin, stopped, brad, 
    topic=136 level=1 (documents=223): slight, apart, scrutiny, collision, debate, faces, course, misled, investors, reality, 
    topic=137 level=1 (documents=191): prick, denier, plausible, absurd, sudden, juliens, -albeit, -pathway, litre, aresholes, 
    topic=138 level=1 (documents=321): chain, drum, concrete, line, gigantic, ear, rail, oct, nw, deter, 
    topic=139 level=1 (documents=326): dance, exhibition, tap, entire, kiss, dawn, ii, danny, scientist, bird, 
    topic=140 level=1 (documents=614): sick, backwards, bend, feel, gas, carbon, china, death, schedule, landowners, 
    topic=141 level=1 (documents=3994): oppose, australian, poll, adani, show, majority, voter, protest, amid, national, 
    topic=142 level=1 (documents=168): ecocidal, deed, bulletin, capella, rockhampton, ne, enlightenment, electorate, trample, farm, 
    topic=143 level=1 (documents=175): ship, importantly, softbank, foxconn, proper, fulfill, load, solar, transferring, 330, 
    topic=144 level=1 (documents=3283): bhp, council, minerals, climate, lobby, membership, australia, association, rio, world, 
    topic=145 level=1 (documents=166): writing, offensive, homepage, myer, hidden, persuaders, picture, gifting, altves, sale, 
    topic=146 level=1 (documents=654): hole, dig, grind, world, let, deep, big, push, benchmark, global, 
    topic=147 level=1 (documents=685): =, officer, executive, tell, govt, environmental, crime, ceo, fail, chief, 
    topic=148 level=1 (documents=276): readmore, consent, contest, tom, employment, jake, landcare, weatherill, forum, listener, 
    topic=149 level=1 (documents=162): needs, mood, fence, leaflet, shopper, cane, office, outside, rum, bottle, 
    topic=150 level=1 (documents=174): 000, un, require, scientist, elect, commitd, suggest, 3of4mainparties, conjob, minimum, 
    topic=151 level=1 (documents=219): lithium, leap, spruiks, opportunity, barnaby, transition, deposit, thermal, jargon, fella, 
    topic=152 level=1 (documents=407): modi, abc, corporation, broadcasting, banana, republic, ambani, rural, journalist, documentary, 
    topic=153 level=1 (documents=170): la, unravel, escondida, eyeball, seeney, terrify, fm, chile, concept, unaffected, 
    topic=154 level=1 (documents=806): elephant, white, waste, hypocrisy, approval, room, gross, export, pursue, infrastructure, 
    topic=155 level=1 (documents=944): decision, investment, final, duck, prospect, carmichael, indefinitely, fade, defer, postpone, 
    topic=156 level=1 (documents=509): credit, roadshow, walk, melb, suisse, involve, bris, canb, syd, brand, 
    topic=157 level=1 (documents=217): operator, lindsay, scary, exact, simpson, whitsunday, opposite, 1st, oppn, hand, 
    topic=158 level=1 (documents=316): medicare, delete, increase, levy, funny, footage, outrage, slo_cashb, abc, modi, 
    topic=159 level=1 (documents=367): 2day, intervention, take, pt, divine, 20k, eurobodalla, congo, flint, beach, 
    topic=160 level=1 (documents=480): wheel, fall, naif, rag, fund, bailout, delay, proposal, taxpayer, dependent, 
    topic=161 level=1 (documents=201): pale, nbn, diversity, amoral, jane, apologies, gut, comparison, survey, def, 
    topic=162 level=1 (documents=142): imaginary, hyperbole, 29.03.slo_year, populist, vs., shortly, sheeps, distinct, scare, redemption, 
    topic=163 level=1 (documents=446): hewson, john, nail, director, coffin, nick, ping, dummy, 7, carolyn, 
    topic=164 level=1 (documents=257): background, hopefully, helpful, property, idk, soros, unhinge, explainer, frothy, undergo, 
    topic=165 level=1 (documents=235): csiro, wheat, yield, impact, trumped, sweetheart, hydrogen, breakthrough, bushfires, happy, 
    topic=166 level=1 (documents=468): cash, negative, flow, idea, project, repay, creditor, life, kind, likely, 
    topic=167 level=1 (documents=495): dumb, model, gear, reduce, bis, -ve, say, shrapnel, claim, judgement, 
    topic=168 level=1 (documents=468): private, viability, railroad, investor, fact, pay, tell, know, jet, need, 
    topic=169 level=1 (documents=1513): future, leave, child, past, invest, evil, fact, will, destroy, financial, 
    topic=170 level=1 (documents=307): beautiful, corby, parli, schapelle, crowd, amazing, morn, step, woohoo, pollie, 
    topic=171 level=1 (documents=150): cnco, queue, earnest, solid, ran, trucks, vet, serviceman, retire, 70, 
    topic=172 level=1 (documents=161): bucket, dye, melanoma, lady, artesian, -she, shove, stopping, ward, gabba, 
    topic=173 level=1 (documents=173): millie, telford, room, tally, cross, anz, july2, update, rs, nations, 
    topic=174 level=1 (documents=260): derail, abt, important, apparently, nuclear, convos, makes, shove, deliver, gunnedah, 
    topic=175 level=1 (documents=245): provider, main, trial, susan, tribulations, claims, shakiest, photo, allegation, probe, 
    topic=176 level=1 (documents=759): hospital, stack, school, free, thermal, board, ceos, endorse, zone, solar, 
    topic=177 level=1 (documents=213): theft, military, woo, mineral, hoo, invasion, allow, sin, austr, indo, 
    topic=178 level=1 (documents=136): military, usa, amplify, risks, extreme, wb, wicked, rethink, shares, eagle, 
    topic=179 level=1 (documents=184): folly, equivalent, mandate, scheme, fashion, entrepreneurial, reek, sleeze, graft, forecast, 
    topic=180 level=1 (documents=571): bhp, qantas, ford, bribes, holden, toyota, rio, shell, tinto, manufacture, 
    topic=181 level=1 (documents=152): petrol, gasoline, ethanol, mile, gallon, mileage, abetz, pump, mobile, split, 
    topic=182 level=1 (documents=138): err, portuguese, persistence, mckibben, alienate, birthday, ur, blood, leeches, thanku, 
    topic=183 level=1 (documents=175): peru, newmont, conga, delgado, advice, maria, 256, 582, gm, authority, 
    topic=184 level=1 (documents=7412): fortescue, metals, ore, iron, group, forrest, fmg, andrew, $, price, 
    topic=185 level=1 (documents=252): 23, rationale, resolve, chairperson, grapple, guess, production, oppose, triple, international, 
    topic=186 level=1 (documents=587): ½í¸³, í, essential, prof, mind, slo_cashillion, claim, counter, journalist, hughes, 
    topic=187 level=1 (documents=227): di, natale, battle, leadership, pivot, shaky, shape, mine/, flashpoint, somewhat, 
    topic=188 level=1 (documents=177): prioritise, objective, yachts, whitehaven, nations, getup, motor, asciano, united, mongrel, 
    topic=189 level=1 (documents=2744): santos, los, video, gta, like, v, 5, city, glng, de, 
    topic=190 level=1 (documents=231): fish, ½í¸ªí, kerala, ½í²ªslo_hash, compensationí, comprehension, live, 13,000, collapse, cause, 
    topic=191 level=1 (documents=196): rare, box, totally, appall, vicious, vindictiveness, white, schlong, defeat, pipe, 
    topic=192 level=1 (documents=197): weak, tonight, deflect, newscycle, meat, fb, exciting, applecart, frolic, righteous, 
    topic=193 level=1 (documents=187): picture, black, illness, diagnose, pneumoconiosis, hunter, wind, wanna, faux, fatal, 
    topic=194 level=1 (documents=188): liable, unprofitable, swipe, glencore, freyberg, coral, exec, savage, peter, ½í»¢, 
    topic=195 level=1 (documents=1260): large, world, coal, build, hemisphere, export, paris, position, idea, alp, 
    topic=196 level=1 (documents=179): park, wane, info, stall, fest, requested, appetite, fracking, kings, things, 
    topic=197 level=1 (documents=291): code, debt, rich, mate, bastard, cut, style, assault, bad, $, 
    topic=198 level=1 (documents=402): review, dan, santos, cinema, film, screen, â, release, operational, dvd, 
    topic=199 level=1 (documents=343): deadline, belong, fail, surprise, miss, chuck, self, disastrous, bin, promise, 
    topic=200 level=1 (documents=269): aslo_cash, find, drama, trouble, ausgov, year, leak, ponds, beggars, belief, 
    topic=201 level=1 (documents=149): falling, abet, aid, fashion, apart, version, corp., financials, fin, mag, 
    topic=202 level=1 (documents=208): piss, wedge, rehab, progressive, blackmail, defer, avoidance, clever, extent, govmnt, 
    topic=203 level=1 (documents=616): newcastle, nice, etc, press, club, closure, unable, decline, national, able, 
    topic=204 level=1 (documents=173): wife, pref, courier, mail, deceive, wheel, qldaahs, husband, badly, bonacci, 
    topic=205 level=1 (documents=192): super, professional, unpaid, proven, whilst, mass, implore, °, stanwell, tradies, 
    topic=206 level=1 (documents=166): whistleblower, barrister, bono, appeal, detention, csg, 9, pro, councillor, petrochina, 
    topic=207 level=1 (documents=319): corrupt, seriously, conclude, politician, office, hold, public, urgently, hunger, food, 
    topic=208 level=1 (documents=185): empire, dropout, school, slo_cashn, magnate, gautam, feck, player, title, narive, 
    topic=209 level=1 (documents=166): suicide, bs, utter, kryponite, reputational, gearing, credibility, luxury, negative, pad, 
    topic=210 level=1 (documents=173): ding, talkback, donation, seen, caller, homeless, leaders, -slo_mention, collect, dong, 
    topic=211 level=1 (documents=184): comms, gillard, doesn't, exaggerate, rudd, ex, practice, bloke, adelaide, earth.slo_hash, 
    topic=212 level=1 (documents=165): weipa, bauxite, wik, xi, colleague, search, alas, this, -on, parlt, 
    topic=213 level=1 (documents=227): exchange, restore, array, development, confidence, gpo, cbd, positive, lease, stock, 
    topic=214 level=1 (documents=163): bitter, bowen, sustain, decline, t, pill, fisheries, appendix, productivity, swallow, 
    topic=215 level=1 (documents=229): n, shld, govmnt, graft, pocket, folly, theirs, wld, earn, awards, 
    topic=216 level=1 (documents=148): thomas, map, longwalls, avon, entitle, edge, dam, professor, nightmare, remarkable, 
    topic=217 level=1 (documents=141): tayla, bravery, strenuously, increase, murry, managment, barnyard, heggarty, retasked, exec, 
    topic=218 level=1 (documents=180): grey, nomad, plot, terrorist, occupy, dastardly, 10,000,000, amazing, infrastucture, 1page, 
    topic=219 level=1 (documents=203): brown, permit, rescind, 60yr, station, jade, effect, moxey, hardly, drum, 
    topic=220 level=1 (documents=133): largest, margaret, fleck, discrepancy, fancy, listen, solidarity, ruined, spake, worlds, 
    topic=221 level=1 (documents=144): sunrise, joã£o, p, verse, hoedown, slo_timepm, â¨â, tour, 142, slo_cashbn, 
    topic=222 level=1 (documents=246): blue, collar, column, north, unify, discussion, greenies, dispirit, tomorrow, size, 
    topic=223 level=1 (documents=192): electric, vehicle, motor, p1, industrialisaion, mclaren, applicable, car, produce, deb, 
    topic=224 level=1 (documents=290): mount, absurdity, climb, take, ¼í¼, ¾í´¥í, ¼í¿­í, arthur, fed, national, 
    topic=225 level=1 (documents=188): jack, unions, mundy, partner, habitat, shorebird, critical, protect&conserve, snelling, acting, 
    topic=226 level=1 (documents=204): brave, sarah, outside, -people, hide, contest, pennings, bane, preselection, establishment, 
    topic=227 level=1 (documents=137): fat, cheque, advert, disbelief, viewer, receive, abc730, shake, minute, thousand, 
    topic=228 level=1 (documents=115): ignorant, eja, dish, bleach, 1000000, backward, sydes, eleventy, severe, brendan, 
    topic=229 level=1 (documents=266): coin, extraction, poison, chalice, waste, anger, clash, resource, value, experience, 
    topic=230 level=1 (documents=163): twin, turbo, engine, luggage, ½í¸¡í, 400, arrive, slo_cashill, foist, harwins, 
    topic=231 level=1 (documents=186): devastation, silent, ecological, rips, heartland, shreds, obsess, lower, limelight, recognise, 
    topic=232 level=1 (documents=147): winners, losers, rinehart, iron, ore, millionaires, kid, millennials, battlers, finalist, 
    topic=233 level=1 (documents=160): success, flyer, distribute, disguised, hob, marathon, nail, son, international, edo, 
    topic=234 level=1 (documents=119): bridge, wander, kick, kerb, alright, aimlessly, mind, gin, quelle, song, 
    topic=235 level=1 (documents=191): embrace, bizarre, extraordinary, rational, symbolism, alex, leyland, bp, portfolio, centrelink, 
    topic=236 level=1 (documents=209): burleigh, nicholls, newman, reasons, awards, bizarre, jairam, ramesh, pile, expose, 
    topic=237 level=1 (documents=241): bond, hv, rehab, abt, frm, revamp, upfront, forfeit, rape, landscape, 
    topic=238 level=1 (documents=298): noise, :|, success, backpacker, bc, train, raise, spend, neoliberal, tax, 
    topic=239 level=1 (documents=180): wang, yusuo, refugee, billionaire, pffft, integrity, fracking, chinese, rust, ring, 
    topic=240 level=1 (documents=159): elizabeth, jj, enviro, ranee, renita, port, demolish, curse, farrelly, english, 
    topic=241 level=1 (documents=125): entity, convert, preaching, 101, plz, ok'd, stalk, jfcygtbk, privatise, dinosaur, 
    topic=242 level=1 (documents=145): journalism, hip, delivery, detail, milestone, penalty, it'slo_hash, btw, unwanted, eff, 
    topic=243 level=1 (documents=223): nab, dismiss, surely, 6,000, 2,400, shed, worthless, signatory, contravene, complaint, 
    topic=244 level=1 (documents=191): general, auditor, woodside, swallow, total, unpaid, royalty, northern, investigate, facility, 
    topic=245 level=1 (documents=212): promote, consistently, downplay, yesterday, fool, slo_hash*0.66, fuel, doll, 34, diminish, 
    topic=246 level=1 (documents=173): nic, student, producer, eagles, batten, bartho, cup, hatch, california, edvel, 
    topic=247 level=1 (documents=545): newman, campbell, pl, lnp, sign, seeney, account, signed, seam, caretaker, 
    topic=248 level=1 (documents=144): batman, curtain, betrayal, quinoa, peeking, km, autobahn, core, execs, ideal, 
    topic=249 level=1 (documents=208): illegally, heaven, forbid, qrc, itinerary, place, capital, burn, explorer, cum, 
    topic=250 level=1 (documents=154): affairs, newtown, boo, sovereignty, cheer, journey, loudest, aboriginal, biggest, st, 
    topic=251 level=1 (documents=200): aslo_cashn, crunch, amid, cash, enthusiasm, cancel, suspension, contract, fact, clermont, 
    topic=252 level=1 (documents=158): phoney, ploy, merely, crisis, limit, access, bonacci, eis, gsg, oracle, 
    topic=253 level=1 (documents=145): questioning, probyn, tilt, oppo, thorough, lib, potash, persistence, contamination, sw1, 
    topic=254 level=1 (documents=149): outback, sour, bet, funeral, plot, guests, thoroughbred, dissident, justin, father, 
    topic=255 level=1 (documents=325): latte, city, inner, stance, online, photo, ½íº²í, roast, soy, oops, 
    topic=256 level=1 (documents=187): replay, winning, rupert, ruler, lloyd, jeff, quintessential, adaniâ, textor, obnoxious, 
    topic=257 level=1 (documents=168): institute, university, excess, victorian, grattan, extinct, spiecies, hypocrisy, general, research, 
    topic=258 level=1 (documents=157): ¼í¾¤, commbank, plane, lynch, flow, crash, tragic, peter, tributes, executive, 
    topic=259 level=1 (documents=255): bow, gracefully, carmichael, king, revolt, peter, reinvent, product, commoditise, coleman, 
    topic=260 level=1 (documents=160): vital, cooperation, nation, international, lifeline, poorest, agreement, paris, australia!go, touchable, 
    topic=261 level=1 (documents=224): ha, w&j, fraser, tiny, sic, illegitimate, fascists, devotion, lifetime, hoo, 
    topic=262 level=1 (documents=135): 20th, realize, nannas, century, arrive, feel, rug, maryland, fleet, convicts, 
    topic=263 level=1 (documents=154): selfish, dumb, conclude, article, idea, aboriginal, spineless, warriors, rabble, goliath, 
    topic=264 level=1 (documents=181): spotted, support4, query, heidelberg, constituents, reason, propaganda, study, collect, achievement, 
    topic=265 level=1 (documents=145): wipe, dorothea, mackellar, actual, negligent, spp, initiative, kellie, 1st, exec, 
    topic=266 level=1 (documents=142): range, imports, dynamic, 543, glassware, svautobiography, rover, annastaciamp, planet, streaming, 
    topic=267 level=1 (documents=156): category, storm, australianseafarers, knw, stronger, rplce, wnt2, hlp, thm, alcoa, 
    topic=268 level=1 (documents=207): cuesta, asx, limited, cqc, â, moorlands, placement, beijing, skies, blue, 
    topic=269 level=1 (documents=126): pant, globe, killing, huffpost, newscorp, millions, wet, immigrant, cotillard, dan, 
    topic=270 level=1 (documents=159): kerry, talks, 100,000, clock, seeing, machines, fatigue, leonardo, melt, hydro, 
    topic=271 level=1 (documents=135): prick, vimeo, petroleum, resist, .slo_hash, scenario, defensible, populace, land.slo_hash, ~28, 
    topic=272 level=1 (documents=123): reward, r&d, understated, unattractive, equation, sydney, legislation, eder, isds, mona, 
    topic=273 level=1 (documents=159): shld, aware, preserve, particular, thread, perf, posterity, shills, grubby, mebourne, 
    topic=274 level=1 (documents=159): lousy, cca, brown, carnell, target, citizen, abbott, rptg, season, indomet, 
    topic=275 level=1 (documents=125): ounce, exports, lnpstill, stopping, impress, mine!not, barrel, worshippers, mammon, ray, 
    topic=276 level=1 (documents=189): rcr, tomlinson, stephen, candidate, hegedus, slam, mention, premier, gasfield, omit, 
    topic=277 level=1 (documents=165): diverse, powerful, peril, retirees, gem, fish, roadkill, beach, preparing, starfish, 
    topic=278 level=1 (documents=160): cathy, session, illustration, wilcox, palm, wilmar, indonesia, sugar, oil, divisive, 
    topic=279 level=1 (documents=253): resign, laugh, seriousness, side, admit, member, sorry, proje, mirth, ache, 
    topic=280 level=1 (documents=171): piss, peace, repetitive, boringly, tammy, management, pt, kingkira, farm, waste, 
    topic=281 level=1 (documents=147): organise, widely, cute, hurly, burly, hella, civilisation, chin, prof, eg, 
    topic=282 level=1 (documents=242): content, word, crook, ash, crooks, women, circumstance, 34, benchmark, 26, 
    topic=283 level=1 (documents=230): perth, justice, refugee, walk, jay, bhuj, mandal, ½í²ª, â¤ï¸âï¸, yuvak, 
    topic=284 level=1 (documents=150): prof, projector, heartening, festive, mood, doondie, koala, industrial, constitutional, simpson, 
    topic=285 level=1 (documents=150): brain, bean, negligence, infant, nobbys, unicef, prospecting, joyce, slo_year-, hancock, 
    topic=286 level=1 (documents=122): debt, billions, apparently, education, prepay, borrow, assist, ohhh, didums, loses, 
    topic=287 level=1 (documents=206): podcast, politics, finkel, talk, live, 11, pub, videos, thur, bangladesh, 
    topic=288 level=1 (documents=127): scottish, bookshop, comm, overland, mgt, surveyed, surveyors, wigtown, angela, invite, 
    topic=289 level=1 (documents=149): iluka, chick, curlews, reserve, backyard, cairns, crown, fruit, poker, bluff, 
    topic=290 level=1 (documents=154): lovely, ½í², slo_mention?í, flab, surely, cut, terror, icon, suddenly, opponent, 
    topic=291 level=1 (documents=293): throw, party, road, access, celebrate, terminal, line, abbot, japanese, bangin, 
    topic=292 level=1 (documents=179): nsw, emily, consent, kickbacks, ½íºí, smells, backs, barnaby, staycee, garbage, 
    topic=293 level=1 (documents=212): shorter, donation, disclosure, ecq, recipient, profoundly, unreconciled, sorry, speech, truly, 
    topic=294 level=1 (documents=182): rope, gamble, msm, excerpt, witness, buying, nt, desperately, limp, rescue, 
    topic=295 level=1 (documents=141): editorial, piece, maranoa, .read, unbalanced, 35, manager, display, lol, picture, 
    topic=296 level=1 (documents=193): raid, afp, pinidu, brown, respond, jacinta, chandrasekera, speer, aretha, trust, 
    topic=297 level=1 (documents=197): beach, father, orange, courier, mail, omaha, dunkirk, grandfather, cast, airlie, 
    topic=298 level=1 (documents=145): persuade, ngp, withdrawal, graceful, bother, islam, groethe, controversy, hotel, gill, 
    topic=299 level=1 (documents=169): department, judge, montana, interior, evaluate, lease, admission, abc, finding, caution, 
    topic=300 level=1 (documents=126): depth, distance, fracking, separation, nationalise, frecklington, brinkmanship, regardless, groundwater, deb, 
    topic=301 level=1 (documents=237): atm, arrive, rope, shutdown, pretend, brigade, update, tayla, unemployed, untie, 
    topic=302 level=1 (documents=125): proudly, inclusive, cyber, literate, diverse, activism, aquifer, untold, divide, backer, 
    topic=303 level=1 (documents=141): suburb, ptn, reratepayers, dfatfundng, concentrate, allez, foi-, /via, lobbyists, patricia, 
    topic=304 level=1 (documents=166): jabiluka, ludlam, 20, scott, describe, resistance, peaceful, succeed, civil, success, 
    topic=305 level=1 (documents=140): cement, interests, yarn, vested, classy, metal, shrapnel, jackhammer, shard, nongs, 
    topic=306 level=1 (documents=205): ridiculous, ping, peddle, aussie, lie, politician, india, rebut, characterisation, arse, 
    topic=307 level=1 (documents=238): blow, passive, approach, resistence, newman, andrews, drag, budget, hole, campbell, 
    topic=308 level=1 (documents=178): sculpture, deaf, award, tone, sea, cottesloe, harrie, horse, fasher, rising, 
    topic=309 level=1 (documents=133): bleed, mongolia, harmless, caesium, license, 137, commonly, lot9, accord, corners, 
    topic=310 level=1 (documents=134): beijing, shuts, switch, natural, thin, ole, evade, winge, entrust, 18/9/13, 
    topic=311 level=1 (documents=124): versus, coincidence, sigh, hepburn, grubs, terrify, 8%+, minds, -pron-, bonn, 
    topic=312 level=1 (documents=192): slo_timepm, tonight, tune, oversell, medium, thx, aka, vid, guest, behalf, 
    topic=313 level=1 (documents=144): credibility, tosser, looking, laws, button, caste, poll, ordinary, meant, anger, 
    topic=314 level=1 (documents=150): better, downgraded, queen, royalist, taker, compare, incompetent, tee, halper, sodic, 
    topic=315 level=1 (documents=147): engage, newtworkig, wash, fools, itch, disease, classify, grandpa, proposition, frost, 
    topic=316 level=1 (documents=147): telstra, sire, leong, job!slo_hash, silver, super, newtown, bandt, revolting, nazi, 
    topic=317 level=1 (documents=154): mouth, gall, grow, lil, message, downstream, highway, glaciers, us40b, tilt, 
    topic=318 level=1 (documents=151): ½í¹í, uranium, annabelle, blom, toot, jellyfish, scale, sez, humanity, technological, 
    topic=319 level=1 (documents=198): approvals, england, free, endeavour, come, cheap, gladstone, treasonous, suckeroo, conventional, 
    topic=320 level=1 (documents=153): sensitivities, cultural, cultures, bogan, cattle, shareholders, -wonder, preprocessor, stand, hypertext, 
    topic=321 level=1 (documents=295): dam, burst, ride, bike, collapse, scream, plus, after, beep, style, 
    topic=322 level=1 (documents=138): sycophant, endorsement, lick, tx, eureka, simper, kowtow, constant, ideology, austn, 
    topic=323 level=1 (documents=174): proposed, admits, benefits, havens, overstating, entitlement, brain, mining, spin, crave, 
    topic=324 level=1 (documents=165): familiar, culture, competition, inappropriate, inmelbourne, attention, having, dor, tabs, lobbyist?slo_hash, 
    topic=325 level=1 (documents=137): mercy, ela, frecklington, govmnt, god, injunction, shill, shills, kubuna, tolukula, 
    topic=326 level=1 (documents=159): conservative, unaware, portray, accountant, spell, random, byelection, extremely, misfit, narrow, 
    topic=327 level=1 (documents=122): soppy, borrow, bhpbilliton, zingers, mover, cowardly, digger, prolly, visibility, bedrock, 
    topic=328 level=1 (documents=152): europe, pa, 150,000, outline, assistance, borgo, bargain, gemma, caratti, quantifying, 
    topic=329 level=1 (documents=177): canberra, st, debate, macquarie, trawl, corridor, prefer, stealing, disclose, panellist, 
    topic=330 level=1 (documents=161): xxx, jane, 100s, different, thx, bay, nwa, 20, michie, terminal, 
    topic=331 level=1 (documents=146): little, runaway, defence, senator, slimy, chase, ham, simpson, homer, remind, 
    topic=332 level=1 (documents=264): rail, unwise, link, eu, subsidising, ex, hedegaard, chief, hostage, hunter, 
    topic=333 level=1 (documents=180): unique, achieve, custom, male, outline, dreamtime, approach, opportunity, instagram, epicentre, 
    topic=334 level=1 (documents=127): ust, poets, building, ncr, additional, cr, kelen, cq, kit, bfp, 
    topic=335 level=1 (documents=215): thakurta, paranjoy, guha, journalist, bravo, website, silence, reportage, try, ellie, 
    topic=336 level=1 (documents=151): donot, quietly, elevate, likelihood, 74, bn, 53, usslo_cashln, poll, railline, 
    topic=337 level=1 (documents=169): desert, alternative, i.e, rightfully, inland, dictator, cleared, flora, disgusting, invasive, 
    topic=338 level=1 (documents=159): legacy, angels, judge, on?slo_mention, history, steroid, weep, swans, tee, zug, 
    topic=339 level=1 (documents=123): suit, marry, rainbow, guatnam, dress, knob, gay, clueless, upstart, justin, 
    topic=340 level=1 (documents=148): wanglan, jangilou, consent, submission, greatest, predict, defiance, whopping, outpouring, 22,700, 
    topic=341 level=1 (documents=128): crew, shed, fridge, aha, cfs, vandal, assemble, sparkke, unknown, vomit, 
    topic=342 level=1 (documents=173): boycott, wales, artfully, bulla, mainstream, demolish, pig, burden, argument, pair, 
    topic=343 level=1 (documents=140): occur, resist, flare, smoky, telemetry, wellheads, assure, politicians, supports, immediate, 
    topic=344 level=1 (documents=143): mal, scrub, donaldson, suitable, rubbery, acf, ½í¸¬, eraser, qld.í, epbc, 
    topic=345 level=1 (documents=236): warren, mundine, aboriginal, angels, entsch, tourism, commentator, silent, guardian, yesterday, 
    topic=346 level=1 (documents=162): experts, switzer, neg, opposing, amci, anglo, vie, consortium, american, bhushan, 
    topic=347 level=1 (documents=164): apply, general, cream, 60-million, throughput, increase, invalid, 50-million, automation, input, 
    topic=348 level=1 (documents=677): visa, india, deny, 457, story, journalist, taxis, bout, hands, worker, 
    topic=349 level=1 (documents=186): hack, quiet, toast, pimp, hands, strike, deadline, heart, pr, badass, 
    topic=350 level=1 (documents=174): diy, fury, expensive, roof, leapfrog, centralise, africa, solar, ovr, stupendously, 
    topic=351 level=1 (documents=223): stupidity, sheer, lunacy, assess, utter, banks, kickback, invitation, venture, pour, 
    topic=352 level=1 (documents=147): ½í´í, arrogance, tuvalu, cause, pm, graze, railline, absolutely, spent, cq, 
    topic=353 level=1 (documents=135): ½í±í, heidi, misdirection, caroline, uytendaal, tks, 16, file, eat, mcguire, 
    topic=354 level=1 (documents=145): ahem, laurel, rest, damn, tylden, pasture, slo_hash, filly, lush, ecosystem, 
    topic=355 level=1 (documents=154): director, dutch, windmill, tilting, secret, journalism, investigative, michael, quadrant, eag, 
    topic=356 level=1 (documents=161): justice, comedy, steven, oliver, diligence, cfmeu, black, biz, mis)management, timber, 
    topic=357 level=1 (documents=150): reductions, meaningful, mini, guarantee, emissions, govnments, flog, symbol, watch, crook, 
    topic=358 level=1 (documents=135): telstra, building, jm, saturday, farking, protests, mullen, divided, ½í·í, 98.1, 
    topic=359 level=1 (documents=191): kristen, labyrinth, unpicking, micheal, amy, ppl, chance, queenslanders, scholarships, colonial, 
    topic=360 level=1 (documents=130): australias, carried, raw, moron, weaken, nickel, unfounded, feed43, crap, questions, 
    topic=361 level=1 (documents=156): sparking, cecilia, berg, outgunned, panel, plenary, tide, compilation, contractor, mentally, 
    topic=362 level=1 (documents=140): observe, ineligible, laura, ministers, whitehaven_itvslo_year_vimeo.1, jp, narayan, embed, vimeo, newmont, 
    topic=363 level=1 (documents=160): pray, parish, chaplains, school, but, exception, ifs, backing, swamp, incompetent, 
    topic=364 level=1 (documents=127): rabbit, torch, son, barbeque, burrow, aboriginals, -slo_hash, definite, piss, ya, 
    topic=365 level=1 (documents=143): leaf, insight, lettuce, properly, seriously, damp, decoding, dv, fig, chart, 
    topic=366 level=1 (documents=146): fiction, anastacia, clueless, exist, patter, fan, sale, irrelevant, critic, feeling, 
    topic=367 level=1 (documents=133): musical, bollywood, twist, elder, rod, smells, rain, curtain, slo_cashbillion, prawn, 
    topic=368 level=1 (documents=188): straw, camel, openly, grasp, break, clutch, criterium, babble, sustainable, here&overseas, 
    topic=369 level=1 (documents=142): hopeland, leaks":-, motivation, bo, santooos, unsavoury, malice, conscious, feels, honest, 
    topic=370 level=1 (documents=150): morally, unjustifiable, scientifically, poem, typo, droll, drilling, desperation, moves, rules, 
    topic=371 level=1 (documents=210): largesse, toon, properly, rein, arun, jaitley, ngos, competitor, decent, abet, 
    topic=372 level=1 (documents=124): quick, wtaf, urgent, forgo, clivepalmer, breaching, flick, committments, ½í¹, cq, 
    topic=373 level=1 (documents=145): impossible, instos, shares, pointless, fishers, c7, coffer, repeal, canavans, inconsistency, 
    topic=374 level=1 (documents=142): beef, efficient, determine, libs.+, downes, goulburn, confrontation, brumby, nats, property, 
    topic=375 level=1 (documents=158): sam, qt, cheaply, slo_timepm, ramp, birth, d, survey, grubby, ph, 
    topic=376 level=1 (documents=133): retirement, coastal, hub, japs, busselton, trample, fly, vibrancy, influx, zionist, 
    topic=377 level=1 (documents=118): payroll, toxfree, cont, lecture, replay, severely, karisto, and/or, stalemate, blunt, 
    topic=378 level=1 (documents=130): millennials, savvy, datum, minehack, attract, bankroll, âï¸, tackling, needs, â­values, 
    topic=379 level=1 (documents=137): theory, conspiracy, delusional, paranoid, invent, context, portal, 1/01/slo_year, complaint, instance, 
    topic=380 level=1 (documents=138): desperately, broadly, exclusively, propaganda, employment, desperate, caroona, seek, reinvent, substantial, 
    topic=381 level=1 (documents=150): fr, unfundable, travesty, pissy, bureaucrat, gummint, abbfuck, prospect, woohoo, dive, 
    topic=382 level=1 (documents=145): corporation, slick, erode, maneuver, double, standard, truffles, silent, sellout, trust, 
    topic=383 level=1 (documents=146): quest, seats, green, lemming, +5.6, ctrs, 8am, summary, launder, caddy, 
    topic=384 level=1 (documents=119): fracking, adhere, 40%+, restriction, chicken, hee, sayí, 96, ½í¸, imani, 
    topic=385 level=1 (documents=153): bastards, bribes, corporation, standing, actuall, toxic, fuck, nothing!making, raiders, economy, 
    topic=386 level=1 (documents=133): molecule, communist, shanghai, 11, adelaide, cred, gui, subsequently, dec, sth, 
    topic=387 level=1 (documents=163): reconciliation, rap, apparent, discussing, elevate, scared, abetz, sham, bar, albatross, 
    topic=388 level=1 (documents=183): dignity, heritage, nation, insult, aspirations, dream, endless, millennia, utopia, bountiful, 
    topic=389 level=1 (documents=125): alberto, meltdown, calderon, orica, sorrow, pilots, sadly, pablo, inner, escobar, 
    topic=390 level=1 (documents=151): wahoo, galiliee, put, salutory, inspiration, qcoal, sooo, hariharpur, tdu, pander, 
    topic=391 level=1 (documents=246): fortescue, forrest, christmas, dave, creek, rain, airport, 0.2, bar, telfer, 
    topic=392 level=1 (documents=137): sleeve, yep, rest, funds, irony-, ½í¸, conveyor, allegedly, para, regardless, 
    topic=393 level=1 (documents=126): granny, famous, bold, audrey, turducken, critique, whore, basic, folks, gandhi, 
    topic=394 level=1 (documents=147): meaningless, no.4, facts, light, green, oresome, graham, winners, reynolds, logicams, 
    topic=395 level=1 (documents=184): respected-, escape, getout, slo_mention-, logo, affiliate, wants, moniker, authority, nsw, 
    topic=396 level=1 (documents=164): magic, countdown, wield, dark, dip, salary, homework, wickham, final, centre, 
    topic=397 level=1 (documents=146): revolution, helen, feminist, unfinished, garner, columnist, curse, incl, anne, stuff, 
    topic=398 level=1 (documents=134): met, 30yrs, prominent, cough, furguson, marcos, brad, collective, relieve, :0, 
    topic=399 level=1 (documents=126): lt, ¾í´í, sane, spirit, dos, excuse, 45, rocky, mclaren, latest, 
    topic=400 level=1 (documents=166): backup, replication, repeat, kicking, ttu, slipper, globe, entertain, siren, thriller, 
    topic=401 level=1 (documents=132): snivel, actual, extremely, gloat, bright, agriculture, reliable, private, vigilante, psychopath, 
    topic=402 level=1 (documents=210): greens, channel, invite, 9, love, participate.slo_hash, debate?phon, exclude, election, advertorial, 
    topic=403 level=1 (documents=137): skeptic, bohena, kidney, soldiers, sweat, display, selective, confident, bloody, regeneration, 
    topic=404 level=1 (documents=136): disgusting, rend, intimidatory, tactic, rental, sort, property, mayor, emtpy, inflate, 
    topic=405 level=1 (documents=145): sutherland, enthusiasm, peever, strength, core, ethic, cbs, ch, fo, inoculate, 
    topic=406 level=1 (documents=148): gunshot, wanna, lefty, click, noise, register, predictive, text, astonish, diversify, 
    topic=407 level=1 (documents=125): en, headline, internationally, wrong, francais, safe, farm, up2thisevil, despair, yard, 
    topic=408 level=1 (documents=179): rtí, negotiable, ½í±, science, crucify, grasp, politicians, future'll, lord, buffet, 
    topic=409 level=1 (documents=137): ccrap, infamous, shelf, diabolical, measure, pwc, hide, memebers, woot, roots, 
    topic=410 level=1 (documents=133): alaska, bulldozer, silence, restart, legislation, karma, consider, depending, sleeper, 0.1, 
    topic=411 level=1 (documents=197): blind, grandchild, cc, thankyou, deaf, freddy, ignoramus, ruth, unpopular, sale, 
    topic=412 level=1 (documents=139): raffle, club, ppls, n, fundraising, workers, meat, weave, fav, liar, 
    topic=413 level=1 (documents=124): tuna, weigh, minerals, mayhem, iv, millionaire, artist, shortage, santimonious, rehydration, 
    topic=414 level=1 (documents=141): spruiking, quality, playing, aljazeera, feature, russian, roulette, guest, insight, tuesday, 
    topic=415 level=1 (documents=149): succinct, lining, summary, greatly, serial, ipalnp, equate, rapist, version, charter, 
    topic=416 level=1 (documents=130): partnership, blood, rio, vested, thinking, medicine, recess, utterly, spot, incentive, 
    topic=417 level=1 (documents=146): here?nsw, slo_hash.slo_mention, newgreens, finalists, capital, interface, ½íµºí, qrc, ra, 42, 
    topic=418 level=1 (documents=153): hearted, prediction, faint, afford, icon, -4, infamy, contain, -7, -3, 
    topic=419 level=1 (documents=124): ½í¸, minker, meí, please, mob, clone, statements, crumble, nntt, piss, 
    topic=420 level=1 (documents=167): cement, permission, coral, palaszczuk, grants, bleached, begin, milling, powder, seal, 
    topic=421 level=1 (documents=166): carry, photo, cleanup, barra, brazil, longa, rake, workers, supply, filth, 
    topic=422 level=1 (documents=143): theme, pot, women, stirring, dreamin, trinket, theyr'e, output, buoyant, doors, 
    topic=423 level=1 (documents=137): 1.4bill, written, transit, harrassing, erratic, linear, curse, quelle, decade, campo, 
    topic=424 level=1 (documents=155): terry, woronov, campus, benedetta, brevini, ââ, sso, julietí, ½í¸, discourse, 
    topic=425 level=1 (documents=133): zionist, religion, domination, sam, particular, christian, choir, powell, xiangmo, dj, 
    topic=426 level=1 (documents=155): tomrw, groundbreaking, plate, utterly, gym, ambulance, ado, bout, brass, plaque, 
    topic=427 level=1 (documents=133): vaxxer, charis, talent, stealth, inaccuracy, awks, boehm, utter, slant, prominent, 
    topic=428 level=1 (documents=154): persist, royal, comm, fricking, s, bad, investment, bank, cede, singe, 
    topic=429 level=1 (documents=118): healthy, breakdown, edited, setback, unreconciled, thinking, crank, frontier, wanna, kindly, 
    topic=430 level=1 (documents=156): mln, altogether, worst, 150, quiz, hoping, em, circus, rc, belligerent, 
    topic=431 level=1 (documents=120): capable, practical, meme, 120, mitigation, uncomfortable, swallow, mgmt, tco2-e, alberta, 
    topic=432 level=1 (documents=130): ½í¸, neurotics, ½í¸í, preciousness!í, atypical, purse, frowing, in2, slo_url””woops, bury, 
    topic=433 level=1 (documents=136): suzuki, ominous, temp, graph, violently, manhandle, peacefully, debut, foretell, mr., 
    topic=434 level=1 (documents=218): downer, agreement, mutual, edi, initiate, consider, cancellation, claim, finance, confirm, 
    topic=435 level=1 (documents=148): dr, abel, ai, lt, anodic, nanoporous, alumina, coauthor, boardwalk, optical, 
    topic=436 level=1 (documents=140): 2day, unviable, up, ante, charade, tripod, tricky, ongoing, whc, perceive, 
    topic=437 level=1 (documents=121): ccs, gavin, yeates, saskpower, foreseeable, highly, recommend, canadian, acknowledgement, president, 
    topic=438 level=1 (documents=154): `, unhealthy, organisation, pathology, suffer, corporate, shorten, self, annoy, i.e, 
    topic=439 level=1 (documents=148): donna, pressure, ahem, reports, internet, overwhelmingly, pension, evasion, deceit, infinity, 
    topic=440 level=1 (documents=153): slope, slippery, african, guard, socialism, bitcoin, willingness, gaming, workmate, broker, 
    topic=441 level=1 (documents=124): independents, liberals, changed, disguise, utter, fundraiser, entrench, ghosts, ot, voting, 
    topic=442 level=1 (documents=126): contact, issues, divided, chemical, olympic, damâ, kills, displacement, plans, mebourne, 
    topic=443 level=1 (documents=169): thorpe, log, lidia, sentiment, stron, program, pro, gadfly, generous, straddle, 
    topic=444 level=1 (documents=138): improvng, choir, additional, alliance, brenda, mk, keyword, projection, ur, superfluous, 
    topic=445 level=1 (documents=131): theft, albert, sarcasm, punter, ¼í¾º, artist, safeguard, derek, ¼í¾¶í, hellooo, 
    topic=446 level=1 (documents=116): kg, distribution, gouge, maritime, murky, instit, hoist, institutes, solve, 45gw, 
    topic=447 level=1 (documents=159): clarification, watto, bse, sarcastic, restock, innovation, lady, prolly, blend, lipstick, 
    topic=448 level=1 (documents=130): despair, answer.68,000, rorts, h'ever, qn, livered, interact, sooo, dribble, it.slo_hash, 
    topic=449 level=1 (documents=167): stoodup, evenhere, readstatementhere, council, home, disruption, occur, elses, disruptor, ofcourse, 
    topic=450 level=1 (documents=131): shithole, reverse, author, 62%oppose, previous, ally, elect, wnr, emma, wired, 
    topic=451 level=1 (documents=175): pics, article, â, database, concoct, nsw.santos, stimulus, literally, objection, 90, 
    topic=452 level=1 (documents=152): putrid, canada, stench, ghunt, vim, word, aid, e.g., clinic, solidarity, 
    topic=453 level=1 (documents=132): patient, jarrod, fans, mins, digging, brit, notes, survival, conjugation, ass, 
    topic=454 level=1 (documents=137): britain, tom, tai, barnden, swann, david, eja, qon, decolonised, independence, 
    topic=455 level=1 (documents=163): injure, revenge, qld&australia, blowback, laborer, correct, foreignlabour, wth, load, rank, 
    topic=456 level=1 (documents=120): clue, caving, disgraces, moira, williams, shld, cldnt, avow, monsanto, lnps, 
    topic=457 level=1 (documents=150): terry, mccrann, retweeted, caves, hrh, australis, back, weâ, mammal, extinction, 
    topic=458 level=1 (documents=129): rehabs, ha, 51,000, assurance, ruin, cup, 8, viral, coffee, give, 
    topic=459 level=1 (documents=130): ½í·³, follower, ¾í¶í, decisive, retweeting, opec, avid, forâ, idiocy, grasp, 
    topic=460 level=1 (documents=128): .slo_hash, reduce, rock, us1.047billion, loss-, optimism, backflipping, jam, fcuk, bihar, 
    topic=461 level=1 (documents=144): offensive, twitter, irl, equality, glare, honesty, uppity, typing, honest, distraction, 
    topic=462 level=1 (documents=150): 41, poll, developing, slip, ceasefire, feels, truly, capture, manufacturer, bb, 
    topic=463 level=1 (documents=164): gilbert, kieran, phrase, nervousness, thinking, ms, regularly, dev, morrisette, study, 
    topic=464 level=1 (documents=137): beg, international, hardware, hack, mriwa, 28, word, â, differ, idiocy, 
    topic=465 level=1 (documents=156): porkchop, pc, entree, fmr, everybody, casino, â¤ï¸â¤ï¸â¤ï¸â¤ï¸, enforce, speaker, advertise, 
    topic=466 level=1 (documents=143): deeply, thot, muppets, wide, alien, protestâ, donations?slo_hash, wut, writeâ, â, 
    topic=467 level=1 (documents=171): wangan, downright, jangalingu, treatment, disgust, lie, -criminal, jingalu, crusader, caped, 
    topic=468 level=1 (documents=136): injury, ½í¸, 3rd, binary, speculative, abomination, speed, ssm, scepticism, logo, 
    topic=469 level=1 (documents=126): latest, consume, fitzroy, egg, pub, staver, 750mw, oversubscribed, gop, bhadla, 
    topic=470 level=1 (documents=120): plz, dayy, surreal, 30k, convergence, unlikely, samaris, hatsoff, gailee, probably, 
    topic=471 level=1 (documents=130): ½í¸¤, plane, powerprice, penaltyratescut, brandisdiary, 16days, sparkly, wayne, promote, v., 
    topic=472 level=1 (documents=130): scramble, quoll, python, hollywood, version, iconic, olive, waggaâ, nominee, operational, 
    topic=473 level=1 (documents=129): retweets, influencers, 104, dee, chevron, headquarter, africans, lt, green, chart, 
    topic=474 level=1 (documents=119): daily, feeney, luck!í, outrageousness, stephen, laggard, infinitesimal, ½í±, offset, solve, 
    topic=475 level=1 (documents=152): plane, charter, talking, asap, mpa, -slo_hash, ideal, legitimate, aero, veritas, 
    topic=476 level=1 (documents=138): fascist, late, dole, wing, billionaires, treason, yeppoon, initially, grandchildren?"slo_mention, preserve, 
    topic=477 level=1 (documents=147): debt, fun, slo_cashln, subsidies, cuts, murdoch, highest, combank, seemingly, 185, 
    topic=478 level=1 (documents=126): overwhelm, sturgeon, tackling, nicola, overview, calma, overwhelmingly, obligation, constant, inv, 
    topic=479 level=1 (documents=186): juru, enterprises, kmyac, finding, oric, pbc, abbot, administration, ilua, mirage, 
    topic=480 level=1 (documents=141): electricity, joe, superannuation, chalk, skeptical, fortescue, recycler, enter, taxpayers, lousy, 
    topic=481 level=1 (documents=131): events, festivals, bronze, relatively, lightly, rust, dlc, sucks, mcgowan, herr, 
    topic=482 level=1 (documents=163): bhp.ax, blt, fpo, indi, respectful, fo, methodology, sage, cathy, volunteer, 
    topic=483 level=1 (documents=131): stories, favourite, fixate, coco, convicts, oil$, pace, bullcrap, grey, battler, 
    topic=484 level=1 (documents=146): zero, project$, figure$, govs, 93, towers, dets, swamps, springs, quid, 
    topic=485 level=1 (documents=143): norway, incl, kepco, insurer, 13, klp, trevor, sykes, bh, 930, 
    topic=486 level=1 (documents=130): da, bergs, joshin, <3, tour, heres, restrict, fried, ahhh, liers, 
    topic=487 level=1 (documents=133): thieve, sustainability, barnyards, fess, whatshisface, crucially, legion, plenty, confused, volley, 
    topic=488 level=1 (documents=168): reception, icey, 2day, datum, conference, forgive, apologist, handshake, thisí, reprehensible, 
    topic=489 level=1 (documents=164): denutjob, russian, alert, dutton, conroy, inconsistency, blink, futurerail, pablo, dogland, 
    topic=490 level=1 (documents=107): boq, optimistic, naively, ferret, createslo_year0, terry, ltrs, slo_cash+, westpac, smh, 
    topic=491 level=1 (documents=129): xpo, govtsurgent2rtn2representintheirown, yolgnu, riot, mundine, warningsbutevidence, gove, damsuspect, condemn, provesnoaction?another, 
    topic=492 level=1 (documents=157): loop, mumble, revolt, calm, margaret, annoy, usual, storey, rebels, sacrifice, 
    topic=493 level=1 (documents=146): lesson, content, surreptitious, utterly, contemptible, regulatory, pal, simply, statesmanship, spain, 
    topic=494 level=1 (documents=138): eg, breaches, exclude, talks, obstacle, plea, develope, wld, natl, told, 
    topic=495 level=1 (documents=149): 4/4, 9.15am, reminder, animal, son, belt, greedy, absolute, 14yo, collaborative, 
    topic=496 level=1 (documents=153): six!!!í, censor, ½í¹, pa, queenslander, spain, wealthy, citizen, tape, boomers, 
    topic=497 level=1 (documents=118): nsa, unaware, disclo, integrity, clarity, firb, linor, vswans, reconciliation, cumulative, 
    topic=498 level=1 (documents=140): zedlines, trumped, mayors, belated, offence, clyde, feasible, bight, reduction&got, heckle, 
    topic=499 level=1 (documents=134): smog, gigantic, bin, cray, puts, ab, millions, mongolia, aboriginal, injure, 
    topic=500 level=1 (documents=152): incredible, runs, coral, bullet, execution, ludders, mind, complicit, iff, rigorous, 
    topic=501 level=1 (documents=143): underwrite, ethic, generous, vote, guess, suicidal, capitalism, game, san, decimate, 
    topic=502 level=1 (documents=142): arse, yeppp, baird, peach, f#%king, kissing, troglodyte, babe, quality, instigated, 
    topic=503 level=1 (documents=125): team, monstrosity, marnti, warrarnja, warajanga, shelter, free, partnership, joh, kind, 
    topic=504 level=1 (documents=137): pepper, spray, ease, sylvia, unprecedented, earle, kerri, 21min, jim, innovations, 
    topic=505 level=1 (documents=116): respect, happen, entrust, themed, roadblock, email, cumulative, scurviedslime, devastate, cosmetics, 
    topic=506 level=1 (documents=143): bugatti, chiron, overlook, shite, syd, ahhh, organic, k, doom, ballarat, 
    topic=507 level=1 (documents=151): spends, nyes, ley, co, gives, character, right, commandeer, wedding, audio, 
    topic=508 level=1 (documents=132): bane, journo, bought, shoulder, descriptor, unusual, hills, bipartisan, vague, ½í²í, 
    topic=509 level=1 (documents=124): pearce, lara, m, nowadays, impairment, 45, fletcher, nzd, dismissal, audience, 
    topic=510 level=1 (documents=153): hazira, tribunal, damage, slam, lambast, ngt, -v-, natl, group, horrendous, 
    topic=511 level=1 (documents=144): affair, khemlani, questions, dfat, wtfru, unbankable, rex, connor, radar, echoes, 
    topic=512 level=1 (documents=136): going, socialist, underwrite, meme, activism, we're, won't, built, joins, ya'll, 
    topic=513 level=1 (documents=130): daft, shuffle, deckchair, final, crims, sarah, shawan, nasdaq, sap, hammond, 
    topic=514 level=1 (documents=158): seat, wyndham, blackmores, extent, widodo, score, injuction, groups, slo_year0, pal, 
    topic=515 level=1 (documents=142): donations?slo_hash, myth, entrepreneur, brawl, alternative, melt, baulk, beef, tigres, harmless, 
    topic=516 level=1 (documents=130): rebuke, table, sing, uk, legislation, smear, wet, vigilant, bil, pussyfoot, 
    topic=517 level=1 (documents=133): ray, hadley, cg, .slo_hash, meat, roboanut, rachel, rick, cooke, countries, 
    topic=518 level=1 (documents=114): whip, leaked, taint, hysteria, returns.slo_hash, greenie, tax?why, misinform, urgently, 6mth, 
    topic=519 level=1 (documents=132): capitalism, bidder, uncontrollable, sewer, stamp, dog, cup, filth, damage, slo_yearbhp, 
    topic=520 level=1 (documents=131): te, de, cuesta, ®, co2, add, boã, ser, weightless, mena, 
    topic=521 level=1 (documents=126): cont, welcoming, pundit, tradeswoman, 77, godbothering, slo_cash,000,000, complexity, stir, minion, 
    topic=522 level=1 (documents=124): ross, assure, upset, zen, telethon, tram, ex-$bhp, longevity, confrontational, calabrian, 
    topic=523 level=1 (documents=123): garner, mnutes, conman, shonk, unclear, culture, behindlife, shoe, publication, campagin, 
    topic=524 level=1 (documents=159): agendum, manipulate, katherine, reader, combine, murphy, nations, cold, pollbldger, pool, 
    topic=525 level=1 (documents=120): deja, vu, peter, distribution, qalp, favorite, consumer, undermine, similar, dumbarses, 
    topic=526 level=1 (documents=133): dire, consequence, brenda, onthemoon, scientists, likely, conclusion, partly, grasp, shamble, 
    topic=527 level=1 (documents=144): kumar, upfront, susheel, thrust, secretary, substitution, policy, cm, pear, charter, 
    topic=528 level=1 (documents=107): blackstone, stun, vocãs, se, grace, 2ser, 5yrs, shit, putas, grounds-, 
    topic=529 level=1 (documents=140): qldlabor, cool, potato, evaluate, shall, f}#%ing, ½í¹í, recognition!í, ½í¸ps, waffle, 
    topic=530 level=1 (documents=160): tianjin, explosion, tut, last, prediction, ounce, seem2, english, rainbow, sumthin, 
    topic=531 level=1 (documents=112): bid, greeny, grim, parable, bleat, spam, coke, vizhinjam, unimagined, depth, 
    topic=532 level=1 (documents=142): backflip, explains, heaven, plainly, ch, late&incomplete, carmicheal, vile, bias, dna, 
    topic=533 level=1 (documents=125): fairfax, chalmers, groubdwater, submit, frightening, adana, myefo, feotid, woolworths, glitter, 
    topic=534 level=1 (documents=159): sri, lanka, persistent, takeover, suitor, shop, maldives, easter, nuno, violin, 
    topic=535 level=1 (documents=142): modernity, koalas, harmonious, selling, harmony, modern, apocalypse, crap, cave, mehta, 
    topic=536 level=1 (documents=115): deficiency, registrant, brief, trzebski, continue, impress, .slo_hash, syndrome, prof, robert, 
    topic=537 level=1 (documents=122): download, itunes, apple, philippines, luiz, sync, copy, precisely, icloud, deployment, 
    topic=538 level=1 (documents=146): mirboo, alliance, north, proud, coord, member, leigh, effort, newmont, dk, 
    topic=539 level=1 (documents=131): imani, sponsored, intensify, parasite, enironment, afford, offend, that`s, cumbria, pouring, 
    topic=540 level=1 (documents=131): covfefe, yeah, trek, bigtime, bruce, abusive, joyces, watching, enrage, spokesman, 
    topic=541 level=1 (documents=142): toyota, wldnt, ½í¸, populate, bunbury, frame, pl, finals, lap, symbol, 
    topic=542 level=1 (documents=144): appropriately, name, cyclone, exxon'ss, paladini, selina, iceberg, ward, sicken, parliament, 
    topic=543 level=1 (documents=157): fuels, tread, sayin, dam, pee, huh, furiously, corporations, pick, trevor, 
    topic=544 level=1 (documents=128): species, violation, denmark, stun, created, horse, boycott, preservation, yeh, disaster, 
    topic=545 level=1 (documents=116): lno, lol, earring, dean, centr, um, wq, conservationists, childish, idjits, 
    topic=546 level=1 (documents=138): unprofitable, shelf, vicforests, ecologically, flaw, tshirt, bitter, pretend, credible, document, 
    topic=547 level=1 (documents=155): pesky, breath, tosser, axe, favor, decent, joes, slavishly, puppets, hazard, 
    topic=548 level=1 (documents=137): coffee, beauty, wheat, artist, -pron-, meat, fundraise, scenario, iluka(ilu, eventual, 
    topic=549 level=1 (documents=148): yowza, common, dinosaurs, mac, embarrassment, mismanagement, willful, htt, focus, rail, 
    topic=550 level=1 (documents=151): harlee, badass, generously, detective, stump, arid, anger, sprite, prolong, fault, 
    topic=551 level=1 (documents=122): colonialist, qu, enjoy, stealin, remember, billion$, mantra, technology, big$$, confidence, 
    topic=552 level=1 (documents=102): courageous, factcheck, shove, gov, landowner, bail, ep, cange, kidman, boon, 
    topic=553 level=1 (documents=123): pt, forest, harding, storage, liars, scientist, scientists, scumbags, precedent, cos, 
    topic=554 level=1 (documents=133): landslide, ftw, enthusiastic, internet, broadband, absence, sq, joggers, related, b, 
    topic=555 level=1 (documents=107): luncheon, commbank, ugh, normally, teks, ceil, surprise, ½í¸, swap, terrorism, 
    topic=556 level=1 (documents=135): code, eligible, plz, stor, 1:1.7, cater, pictures, mothballed, 1/2, sentiment, 
    topic=557 level=1 (documents=143): grandchildren, short, negotiable, reflect, shirt, terrorist, whiteoak, wobbly, wildcats, ½í¸±í, 
    topic=558 level=1 (documents=141): plate, spawn, solidarity, majeur, acland, brass, stipend, cubic, stimulate, fn, 
    topic=559 level=1 (documents=132): ethan, bhpâ, device, mil, bash, floatation, california, honour, spread, sowing, 
    topic=560 level=1 (documents=136): autocracy, deploy, kloppers, adf, absurd, iv, economics, fecking, competition, feb18, 
    topic=561 level=1 (documents=139): comedy, crock, cos, whoops, backstory, dana, nuccitelli, prophetic.slo_mention, suddenly, reputation, 
    topic=562 level=1 (documents=144): deed, db, whore, labour, derive, mo, notch, shills, doesn't, jab, 
    topic=563 level=1 (documents=148): enquiry, pissant, siberia, unanswered, bastardising, secrecy, unacceptable, concept, propaganda, permanent, 
    topic=564 level=1 (documents=115): nah, diks, fuckhead, taxpayers, mid-30, ipa, holes, 200k, errr, birth, 
    topic=565 level=1 (documents=165): tweed, shire, milne, katie, connect, santosltd, external, ignorant, psa, choke, 
    topic=566 level=1 (documents=133): vulnerable, weapon, instruction, nasser, descend, manufacture, carpetbombs, conference, splits, wood, 
    topic=567 level=1 (documents=133): wagon, attachment, fur, qc, coates, sherlock, ton, hottest, flares, dioxide, 
    topic=568 level=1 (documents=121): insult, needed, experts, archives, gets, feminist, richard, military, 87, queue, 
    topic=569 level=1 (documents=128): imaginative, ndva, obstructive, start, rcg, lately, breathe, enjoy, trust, posted, 
    topic=570 level=1 (documents=107): yup, pattinson, crap, spirit, motivate, brickworks, gosh, haunt, launderer, nrw, 
    topic=571 level=1 (documents=141): tool, ~20, solar+wind+hydro+bio, annual, view, able, development, past, nugent, pretty, 
    topic=572 level=1 (documents=136): 644, dawes, blah, points, cred, persist, terrorformers, birriah, ½í´í, oxfam, 
    topic=573 level=1 (documents=167): vis, hand, act, win, retail, nervous, request, shop, cng, shirt, 
    topic=574 level=1 (documents=133): adjacent, spill, drum, platitude, unconfirmed, firies, leewood, hazmat, rot, horrify, 
    topic=575 level=1 (documents=127): hippy, slo_cash7, hippyhoaxgate, shoulda, january, trend, slo_urlâ, davi, dpspritepalette, britain, 
    topic=576 level=1 (documents=148): quota, performance, theme, decade, gupta, shout, verdict, hint, url, focusing, 
    topic=577 level=1 (documents=166): balhuizen, arnoud, outlook, cco, shortlist, filmmaker, nicholl, fellowships, commodity, screenplay, 
    topic=578 level=1 (documents=164): lights, rd, uselessâ, outstanding, vicky, alexander, luckily, gnangara, racist, threatens, 
    topic=579 level=1 (documents=142): reward, lucrative, outrageousâ, yeppoon, arrogantly, driver, ï¸, ba, feat, .china, 
    topic=580 level=1 (documents=134): cleanup, rife, barracks, men, league, army, hardcore, uncertainty, mission, politician, 
    topic=581 level=1 (documents=137): broadcast, ciobo, handful, bippy, kick, dollarâ, deserves, simone, maud, backfill, 
    topic=582 level=1 (documents=135): treachery, i., tanods, weep, suv, bartho, bugger, forgive, karabelas, iugo, 
    topic=583 level=1 (documents=161): deduction, pre, engagement, harrison, slo_cash6, slo_cash6b, continually, reinforce, namoi, rental, 
    topic=584 level=1 (documents=149): dealer, dob, malone, teen, claimant, cherbourg, feat, patrick, woorabinda, scum, 
    topic=585 level=1 (documents=117): protests, tougher, scott, thankful, siberia, install, retailer, trek, enhance, bridle, 
    topic=586 level=1 (documents=125): prudent, plants, enabler, fansite, mumbal, worksite, listened, politicallly, invasive, shutdowns, 
    topic=587 level=1 (documents=142): bonn, talks, oil, hurdle, manu, ppl, terri, slo_cashbil, ice, beef, 
    topic=588 level=1 (documents=151): races, yabbie, moonie, dress, obscenity, genocide, ethical, destroyed, consumption, adversary, 
    topic=589 level=1 (documents=147): unviable, fk, knows, cease, enought, sucken, tory, rookie, theatre, amalgamation, 
    topic=590 level=1 (documents=151): pesky, idf, troop, corbyn, threatens, ¼í¶í, investments, unlikely, infantry, md, 
    topic=591 level=1 (documents=143): cassette, factory, recorder, countries, administrative, statutes, construction, kelly, laws, beach, 
    topic=592 level=1 (documents=138): blah, qldlabor, persuade, hands, duet, leftist, upside, ultimate, pursue, pder, 
    topic=593 level=1 (documents=161): fta, pmt, argument, enable, bring, miserable, placard, immoral, fkn, ludicrous, 
    topic=594 level=1 (documents=140): curse, dedkrow, cracked, aquifer, h2o, /cough/, anytime, 60years, auditor, search, 
    topic=595 level=1 (documents=136): nell, schofield, director, producer, screening, doco, documentary, 27/3/slo_year, widely, inundation, 
    topic=596 level=1 (documents=146): occupy, cole, emil, european, newcastle, banks, dacy, emotion, capitalism, display, 
    topic=597 level=1 (documents=145): irrelevance, politicked, marcus, defensible, myth, logan, entitlement, ballarat, illusion, google, 
    topic=598 level=1 (documents=138): tarrawonga, pounce, ownership, deadline, wbc, amendment, eco, justin, applications, burning, 
    topic=599 level=1 (documents=148): fascism, softly, equipment, conjecture, students, republican, cliev, players, construct, vella, 
    topic=600 level=1 (documents=116): agony, example, bonkers, calcutta, algo, slo_hash’sbroke, slo_hash’scorrupt, longtime, shark, revise, 
    topic=601 level=1 (documents=135): cops, mute, bmw, ric, usual, elections, skyrocket, 326kw, loony, -graziers, 
    topic=602 level=1 (documents=158): quash, exhibit, pray, household, macdonald, suspicion, camperdown, sub, subscriber, miracle, 
    topic=603 level=1 (documents=126): austmine, ditch, novel, networking, protozoon, airobotics, wespac, ooh, unnatural, earthmovers, 
    topic=604 level=1 (documents=123): stigma, races, gunna, flyers, wooo, proposed, emission, road-, 5,6,7, onslow, 
    topic=605 level=1 (documents=127): turtle, judo, soul, strangle, religious, obsession, turnitup, unfit, obstructionists, four, 
    topic=606 level=1 (documents=121): gov'ment, ciobo, inspiring, geelong, los, freedoms, cup, complaint, song, nike, 
    topic=607 level=1 (documents=139): mouth, insights, run, seal, wah, trouble, priceless, imminently, ass, gc, 
    topic=608 level=1 (documents=119): lang, getting, â­gautam, headwind, save, suggestion, ecopath, grim, selective, controversy, 
    topic=609 level=1 (documents=134): passion, pago, successful, whoop, kirsten, village, obsession, beresford, complicit, pretension, 
    topic=610 level=1 (documents=135): toast, marius, bitch, restrict, hype, true, childish, destroyed, kloppers, complicit, 
    topic=611 level=1 (documents=147): brochure, rebutt, fact, share, politic, fess, elite, unacceptable, frosty, slump, 
    topic=612 level=1 (documents=130): subcontractor, shop, pride, hometown, goon, season, last, thxs, flying, un, 
    topic=613 level=1 (documents=127): present, bludging, trans, dan, pretty, personify, birdie, focused, foe, badham, 
    topic=614 level=1 (documents=135): poke, freydenberg, shoulder, money!more, consumer, organise, start, signed, fabrication, defensible, 
    topic=615 level=1 (documents=155): m2, abuse, perfect, ronaldo, lifetime, starter, bmw, motza, m135i, no'1, 
    topic=616 level=1 (documents=143): uneducated, accountable, buffoon, doh, slo_mentionâí, foxtel, ½í², soil, carnegie, kooyong, 
    topic=617 level=1 (documents=135): socialist, beat, y, 10.14, rabble, tea, economic, inspector, barnyard, bugs, 
    topic=618 level=1 (documents=158): generally, troll, arrangement, viability, disgrace, defending, â, pr, heres, tube, 
    topic=619 level=1 (documents=133): ghg, overpower, place, castoffs, vcap, final, prob, teach, luví, dec, 
    topic=620 level=1 (documents=136): slogan, progressivism, mouth, rba, thinly, doppleganger, disguise, cheap, precarious, increasingly, 
    topic=621 level=1 (documents=132): unjust, mackenzie, resend, unaustralian, inquest, donors, ½í¸â¤ï¸, hoax, fondo, fish, 
    topic=622 level=1 (documents=131): hemmed, constantly, reinstate, incest, ro, alani, android, convos, reports, headphone, 
    topic=623 level=1 (documents=121): widely, bias, wanted, eastern, sprout, 2have, ftw, hotter, embarrassment, lyford, 
    topic=624 level=1 (documents=138): n’t, turd, drawdown, 3.7, murph, whilst, eis, bono, whyalla, ratbag, 
    topic=625 level=1 (documents=130): adjacent, stickers, thankfully, aims, goanna, geiger, hugs, yup, scar, polluters, 
    topic=626 level=1 (documents=145): mdx, los_santos_sikos, gov., reckless, 177, invincible, stinkyrut, sara, freakin, length, 
    topic=627 level=1 (documents=127): choo, inq, witch, minerals, witnesses, divestment, cbr, chattanooga, amendment, discount, 
    topic=628 level=1 (documents=128): jpmorgan, choke, forgive, bidder, retrain, woodside, 6.1.37, turf, 3.12.30, highbury, 
    topic=629 level=1 (documents=116): wake, correction, deleted, ground, ripper, dodger, accidental, sustainable, promoting, infestation, 
    topic=630 level=1 (documents=138): cheery, residual, ftw, hood, grey, :p, tug, guvunmunt, lots, forelock, 
    topic=631 level=1 (documents=142): pussy, complicit, waffle, dilemma, awww, battler, philanthropists, compel, brisi, terrace, 
    topic=632 level=1 (documents=135): ticker, skynews, rofl-, 14,000, this-, cantavan, telcos, spectrum, lockout, taker, 
    topic=633 level=1 (documents=139): broadly, toorak, nationals, /2, album, pioneer, sympathetic, unreliable, opt, next-, 
    topic=634 level=1 (documents=129): ccp, gamechanging, payable, reckons, bro, jr, democracies, swing, rolon, nap, 
    topic=635 level=1 (documents=142): hindu, terribly, yawn, fav, map, explicitly, maintain, retrain, geography, redirect, 
    topic=636 level=1 (documents=139): apache, senators, rider, sing, burial, sold, hariharpur, sneaky, grounds, dart, 
    topic=637 level=1 (documents=144): insult, cynic, poetic, a*se, collection, 2mil, emperor, bludgers, talented, uber, 
    topic=638 level=1 (documents=146): frm, harness, ½í¹, harry, chest, brainwave, evidence, deploy, beat, truckies, 
    topic=639 level=1 (documents=133): 5yrs, mechanism, grace, stock, clever, abolish, fantasy, roadworks, stirling, rds, 
    topic=640 level=1 (documents=128): imogen, ì¶aì¶nì¶dì¶, tì¶hì¶eì¶, ¾í´¢í, patel, behavior, pa, commitmt, irrigation, vaisnali, 
    topic=641 level=1 (documents=143): loop, roof, embarras, arse, effort, powerhouse, tsv, de, lengthen, bne, 
    topic=642 level=1 (documents=163): ~any, lesser, accept, evil"-dom, this~., reason~, dividend, fuck, election, geophysicist, 
    topic=643 level=1 (documents=146): duty, practice, .the, campaigns, qantas, obey, myopic, wildly, exclusive, regain, 
    topic=644 level=1 (documents=131): erik, nurse, ux, entitle, engagementhq, ui, ep6, magnate, homework, rr, 
    topic=645 level=1 (documents=135): slo_cashm, bathurst, coin, national, gun, explanation, stairway, bollycoal, shun, exemption, 
    topic=646 level=1 (documents=114): ep, organics, dr., obvious, blatantly, pack, hyde, bribery, guarantee, metre, 
    topic=647 level=1 (documents=124): info, megamines?adani, aust.needs, 3rinehart, leopold, colaba, closely, megamines?jobs?miningbeingnowautomated, american, opposition, 
    topic=648 level=1 (documents=155): plate, advance, ausgold, stitch, los, criminals, tol, ½í¸, ½í±¢, tough, 
    topic=649 level=1 (documents=115): oi, frail, urban, abt, certificate, exciting, wgich, mayer, second, ~and, 
    topic=650 level=1 (documents=134): lawful, generously, julie, case, confusion, insight, hallows, optimistic, pursuit, westies, 
    topic=651 level=1 (documents=157): slo_hash?slo_hash, 0, automated, correct, mirage, warrior, 4q, literal, nails, acid, 
    topic=652 level=1 (documents=127): dominate, q&a, spar, indefensible, panellist, dubai, known, trust, sinclair, heard, 
    topic=653 level=1 (documents=134): landline, elite, altogether, sorted, smile, immune, protocol, fibre, mi, pa, 
    topic=654 level=1 (documents=105): mariana, editorial, gestapo, bleh, questionable, seth, hny, reader, cope, lag, 
    topic=655 level=1 (documents=133): antiprotest, thatrivals, draconoian, ccrap, thinking, unesco, regard, crow, oppose, malice, 
    topic=656 level=1 (documents=155): cute, reaction, reason, thy, facebook_organic, pollie, 77, thinkst, crook, jo, 
    topic=657 level=1 (documents=125): gardens, conf, bowl, sponsorship, comments, nod, scruple, bougainville, military, urgent, 
    topic=658 level=1 (documents=162): turd, gomeroi, tweeps, speaking, spring, macquarie, appall, tour, treachery, ccrap, 
    topic=659 level=1 (documents=151): ½íµ³ï¸í, intense, emblematic, wipe, thinking, barrierreef, subdivide, gear, enormous, planetkiller, 
    topic=660 level=1 (documents=116): oo, convince, freeby, adanicoalmine, ½íµ¸í, horrify, se, businesses, wealth, gahd, 
    topic=661 level=1 (documents=122): ought, apologise, unreserved, disgusting, backer, shameful, lifeline, insightful, nwnsw, james, 
    topic=662 level=1 (documents=155): freight, centurion, fkn, bath, nigel, reading, nannas, o'brien, 135, champagne, 
    topic=663 level=1 (documents=130): waive, definitely, fairness, reef4-decades, -pron-, @/knag_hunterloop, generously, impact, word, gesture, 
    topic=664 level=1 (documents=148): jobsandgrowth, broadcast, sayin, stoptheboats, mission, â, thiess, platitude, bra, sales, 
    topic=665 level=1 (documents=123): minority, america, perfect, debacle, churchill, admire, ½í¸¬í, alabama, bayern, place, 
    topic=666 level=1 (documents=130): qualification, pretence, hypocrisies, slash, merit, honory, shortens, squiers, kellogg, certificate, 
    topic=667 level=1 (documents=136): ceremony, jagera, capitol, watson, caravan, sam, immeasurably, smoking, machine, jeopardise, 
    topic=668 level=1 (documents=143): xx, reader, muted, ingleburn, sport, potential, intelligent, day17, enogh, graziers, 
    topic=669 level=1 (documents=141): ambition, c’mon, costa, small, rica, â, rehabilitate, toy, nudge, bounce, 
    topic=670 level=1 (documents=115): fiddle, mrx, spanner, dave, jay, boundary, advantage, gandhi, throw, narooma, 
    topic=671 level=1 (documents=146): empire, slo_mentionâí, ½í², vicious, lies, wombat, visitor, crim, bitch, gaol, 
    topic=672 level=1 (documents=131): hide, dougie, adrian, unionist, forest, pursue, oath, embattled, literally, narabri, 
    topic=673 level=1 (documents=147): sensational, y'all, overlook, bergmann, wayne, gooders, cup, division, placement, combo, 
    topic=674 level=1 (documents=149): shitty, hug, students, donations?slo_hash, match, establishment, akubra, parliament, liars, purify, 
    topic=675 level=1 (documents=138): organics, lnps, suggestion, flyer, harass, retreat, reap, visibility, buckland, picture, 
    topic=676 level=1 (documents=119): vested, employ, ffs, treat, miner, ben, retain, lol, veil, companies, 
    topic=677 level=1 (documents=139): wish, goes, doomed, forgets, admire, guest, quickly, church, supportive, afar, 
    topic=678 level=1 (documents=141): er, iinadequate, measure, payout, pursue, winkelman, fires, graham, prevention, giga, 
    topic=679 level=1 (documents=123): -slo_hash, tay, grant, bribes, perpetual, brought, -my, bairdy, selective, james, 
    topic=680 level=1 (documents=146): beijing, misinformation, leadership, dispel, task, businesses, yearn, partners, 3~4, minor, 
    topic=681 level=1 (documents=147): no, petroleum, halal, dna, easily, winter, irony, weep, suitable, aest, 
    topic=682 level=1 (documents=173): choo, lmao, spray, thankyou, hansard, tucker, syndicate, cucroach, mar13, barry, 
    topic=683 level=1 (documents=111): 1/, seats+, vibe, arrcc, affordably, touchid, newtown, chs, epic, 654, 
    topic=684 level=1 (documents=126): queenslanders, blink, colossal, flaky, pleasantly, alice, retweeted, courier, ltr, copper, 
    topic=685 level=1 (documents=122): â­, safety, malign, citizen, lifes, elder, ajobs, unconscionable, display, campaigning, 
    topic=686 level=1 (documents=127): cross, alchemy, sounds, formation, zone, 1bn, pathway, 65, cardio.i, rd, 
    topic=687 level=1 (documents=126): junk, essentially, nasty, status, obstacle, kidston, stubborn, heaps, smell, nws, 
    topic=688 level=1 (documents=127): 255, windows, accidentally, uninspired, ko, patron, definite, renaissance, wasteland, xxx, 
    topic=689 level=1 (documents=154): coin, judge, bs, incentive, fj, prefer, construction, output, enjoyable, duo, 
    topic=690 level=1 (documents=137): lady, corpse, .santos, carpetbagging, eyesopen, optimism, voters-, ferry, bushfires, wetland, 
    topic=691 level=1 (documents=126): ¾í´ªí, dither, allegiance, won't, belong, citizens, rapist, commonly, stopâ¡slo_mentionâí, 76, 
    topic=692 level=1 (documents=140): detail, pip, mkt, dexter, yahoo!7, jackpot, objective, ictd, besieged, rescue, 
    topic=693 level=1 (documents=149): ½í¸í, u'll, proclaim, bipartisan, witness, be?slo_hash, grub, musing, course, tolerance, 
    topic=694 level=1 (documents=146): soil, havn't, coalmines, âï¸, tyre, hat, crp, insolvent, economist, isingapore, 
    topic=695 level=1 (documents=111): christine, wisdom, ambiguity, entrench, joe, remind, foolproof, pensioner, counterpart, ruth, 
    topic=696 level=1 (documents=121): breakdown, implications, newsroom, hydro, fortnight, discontent, coke, beneath, 2day, country."slo_hash, 
    topic=697 level=1 (documents=144): 3.threat, medicare, 1.threat, dutton, 2threat, listen, cyclist, flunkey, shepherd, stench, 
    topic=698 level=1 (documents=129): moon, hell, sharp, lunatics, yuuuge, siren, unicorn, intensity, chicken, jungle, 
    topic=699 level=1 (documents=168): shove, megaton, hilter, ethics, arm, ¼í·¯í, permian, 101, skeptic, autumn, 
    topic=700 level=1 (documents=148): activism, wild, haters, disability, necessity, snowflake, joy, online, snoopdog, punt, 
    topic=701 level=1 (documents=128): accelerant, instability, wrt, bankers, unexpected, cdc, sums, ret, scholar, perfect, 
    topic=702 level=1 (documents=136): vacation, outcomes, luxury, gets, especially, marsh, shooting, humane, horses, replaced, 
    topic=703 level=1 (documents=135): standpoint, nice, depend, bulldust, catenation, mc, undo, definite, manner, pexco, 
    topic=704 level=1 (documents=124): buying, actively, supplement, appin, unbeatable, unbelievable, .will, trade, properties, map, 
    topic=705 level=1 (documents=129): 8,536, blogazine, booth, queenslan, bloggingâ, christmas, uh, stadium, macfarlane, bets, 
    topic=706 level=1 (documents=129): dispatch, sbi, ios10, accountable, outrageous, customisation, doc, venal, steroid, wh, 
    topic=707 level=1 (documents=142): massacre, riverland, plot, teenager, properly, literal, lecture, bedroom, participatory, inept, 
    topic=708 level=1 (documents=127): avo, smash, /via, indulge, toast, unendurable, entertain, stuck, projection, relevant, 
    topic=709 level=1 (documents=131): macaulay, yeppoon, dearly, excitement, mine?slo_mention, worthless'pilliga, les, fukushima, ruthless, shakey, 
    topic=710 level=1 (documents=126): rorting, spells, ½í±¿í, bias, intently, sad, iz, investor, agreed, function, 
    topic=711 level=1 (documents=135): ^, usslo_cashillion, boats, auslo_cash, november, lemming, carelessness, monstrosity, boot, paladin, 
    topic=712 level=1 (documents=138): ½í¸¹í, peoples, whales, chant, carbon, atmosphere, pension, ooh, skilled, ½í¸¹, 
    topic=713 level=1 (documents=150): enthusiastically, idk, elder, combine, mackay, vadra, fear, swing, badmouthed, put, 
    topic=714 level=1 (documents=165): aquatic, .great, blackwater, cheap, tailings, behemoths, synthetic, evaluate, gj, landholder, 
    topic=715 level=1 (documents=139): ross, plaza, whoop, environmentalists, globe, scoff, astound, toss, bitch, gag, 
    topic=716 level=1 (documents=157): unite, landholders, apologise, provision, moosie, blockchain, smug, lifespan, trollbot, ccs, 
    topic=717 level=1 (documents=125): physic, ½í¸¤í, mathematics, serco, friggen, stockbroker, ½í¸¤, privatising, beware, evidence, 
    topic=718 level=1 (documents=148): basket, egg, division, pioneer, frustration, toys, ½í´¬í, skepticism, disadavantaged, verdict, 
    topic=719 level=1 (documents=121): needed, 48, gave, seated, racist, exciting, comments, ecovandalism, angry, park, 
    topic=720 level=1 (documents=156): appropriate, graph, distinguish, quest, terrifying, 19, deferred, shade, fellow, strpung, 
    topic=721 level=1 (documents=110): christian, mack, protesting, saves, sob, thousands, spread, launching, roti, drink, 
    topic=722 level=1 (documents=141): spinner, nowâ¤ï¸, efforts, stacking, barrack, duct, rat, racism, barnabiy, curry, 
    topic=723 level=1 (documents=138): sunglass, numerous, collection, pump, feeling, calculate, tit, smg, concubine, walking, 
    topic=724 level=1 (documents=136): waste, hugger, ultra, existent, odd, yeppoon, ais, hubris, knot, counterpart, 
    topic=725 level=1 (documents=138): task, environment, lip, gifts, miss, abide, dress, symposium, house, dipshits, 
    topic=726 level=1 (documents=140): sorta, unsurpassed, kate, bishop2, tks, savva, tk, sharpfang, app, damascus, 
    topic=727 level=1 (documents=130): closet, skeleton, piwo, communication, spin, refusal, shitload, neighbour, roadshow, jose, 
    topic=728 level=1 (documents=130): fight, cartoon, wifi, ta, aliconsidine, boon, interview, knell, â, colour, 
    topic=729 level=1 (documents=116): turd, knowledge, open2read, .that, conduct, cock, proud, want, source, 3.30pm, 
    topic=730 level=1 (documents=123): c'mon, fo, poo, davis, constantly, sincerely, flat, awhile, karma, blackouts, 
    topic=731 level=1 (documents=132): astronomical, bight, retirement, olly, hilarious, grandkids, conflight, landcruiser, dont, roy, 
    topic=732 level=1 (documents=140): conserve, bonds, 93, tab, bairdy, unstoppable, jpratt27, outlook, lorraine, rehabilitation, 
    topic=733 level=1 (documents=112): petrol, wrap, leonora, auto, makcorp, aline, northern, vern, 7yrs, town, 
    topic=734 level=1 (documents=137): spare, randomly, backtrack, asap, shoe, squirm, interim, turnbullshit, ecommerce, length, 
    topic=735 level=1 (documents=137): paully, sink, angel, insanely, oswal, finally, due, ny, ½í¸³, birdhouse, 
    topic=736 level=1 (documents=130): recovery, millionaire, stonking, doubtful, brinkmanship, incontinent, decarbonize, growing, messy, dessert, 
    topic=737 level=1 (documents=140): official, fm, procure, buffet, try, nswrfs, spruiking, illiterate, vitor, ignores, 
    topic=738 level=1 (documents=119): bear, fishy, backtrack, chip, german, rubbish, potato, reliance, coa, baby, 
    topic=739 level=1 (documents=142): slo_cashbil, clarity, actual, wilson, baron, bj, logo, systemic, outlier, marcus, 
    topic=740 level=1 (documents=150): turd, polish, theirs, hands, scroll, racist, factual, emissions, brainless, vandalism, 
    topic=741 level=1 (documents=136): walker, scramble, blah, pig, entertainment, foyer, mw, tyler, headache, bret, 
    topic=742 level=1 (documents=121): qldlabor, knuckles, bulletin, lgbti, rapped, rider, sightedness, videos, jan'13, slant, 
    topic=743 level=1 (documents=112): stolen, accountable, rural, fraudster, unlikely, travel, heavily, outsource, misusing, relation, 
    topic=744 level=1 (documents=138): .is, liquidate, s.46, murky, beer, targeting, -pron-, insanely, hungry, sincere, 
    topic=745 level=1 (documents=109): slo_hash¤, cat, subscribe, eat, mile, crop, bil, ya, unsurprisingly, slo_yearcewscholar, 
    topic=746 level=1 (documents=129): watched, suburb, history, waaay, equivocate, consistent, /cc, interfere, 1:0, flng, 
    topic=747 level=1 (documents=128): granfondo, riders, mandorah, muppeting, distort, muslim, palaszczuks, permeate, moronic, receives, 
    topic=748 level=1 (documents=116): turtley, utterly, thompson, ugh, totally, aplng, lawfare, menzies, aud900, even, 
    topic=749 level=1 (documents=141): forestry, blatantly, 0.00, transcribe, doomben, champion, bpcc, stink, gambler, dig, 
    topic=750 level=1 (documents=139): kfc, -graziers, media, slump, barnyards, eve, click, keith, definitively, angle, 
    topic=751 level=1 (documents=123): debacle, crowdfunding, believer, investigative, cute, alternative, tow, saga, b'caster/2destroy, suggestions, 
    topic=752 level=1 (documents=109): choose, secretly, zombie, politically, investigative, observation, best, infighting, unemployment, reset, 
    topic=753 level=1 (documents=138): hopelessly, space, plunder, incomprehensible, killing, last, rightly, linkedin, inapproriate, blackthorn, 
    topic=754 level=1 (documents=129): paramount, trish, wetland, spanner, c’mon, ½í´´environmental, grrr, kills, yest, recent, 
    topic=755 level=1 (documents=138): quickly, rude, elections, blunt, bury, stopped, item, caroona, 60mt, 11-year, 
    topic=756 level=1 (documents=130): cray, slo_mention.ified, albo, alan, million$, mansion, harbourside, relations, firmly, shitting, 
    topic=757 level=1 (documents=118): apron, shadow, ceo, quiet, thn, skylineí, equal, twirl, homework, cory, 
    topic=758 level=1 (documents=106): nasty, bids, curve, neglect!â, survey, x, gm, hospital, mccain, wifi, 
    topic=759 level=1 (documents=130): welcoming, vile, arse, -pron-, wristies, resurgence, dimasi, macroplan, embarrass, bus, 
    topic=760 level=1 (documents=152): publicity, taint, holiday, funny, coastline, fool, slippery, unfortunate, hop, polite, 
    topic=761 level=1 (documents=126): didn`t, os, slogan, wrecks, rica, bud, particular, grom, furnace, hear, 
    topic=762 level=1 (documents=153): greatness, van, ideological, dicks, breed, shrink, script, lisa, borrow, daughter, 
    topic=763 level=1 (documents=122): bitch, subsidiary, kerry, lose, keller, precisely, -rio, cyclists, chairman, frontline, 
    topic=764 level=1 (documents=132): xx, illiterate, hail, stolen, billn, social, knell, sharp, customers, dunny, 
    topic=765 level=1 (documents=120): aboard, barn, proposition, bangarra, fondo, tamworth, cities, iluka(ilu, wise, plebiscite, 
    topic=766 level=1 (documents=124): conscience, decim, dale, mariner, boyfriend, forensic, hahah, josh, requirement, intelligence, 
    topic=767 level=1 (documents=116): utilities, eq, chemical, fix, personally, pushcoal, backhander, intend, ganesh, tel, 
    topic=768 level=1 (documents=135): shilling, dickson, sycophant, relentless, wilpinjong, forth, kate, saw, remind, knuckle, 
    topic=769 level=1 (documents=135): alps, wakey, brainless, apoligists, ilua, slo_mention!why, swanny, escalation, coffer, individuals, 
    topic=770 level=1 (documents=132): indication, runt, sparc, dea, alice, honest, tweets, needs, dreamy, robodebts, 
    topic=771 level=1 (documents=121): remember, annap, tht, 77, diplomacy, byron, bacon, 76, brenda, court, 
    topic=772 level=1 (documents=121): linda, houston, scott, o'farrell, follow, want, councillor, oath, modi, liable, 
    topic=773 level=1 (documents=116): snow, fascist, el, brakken, fuss, shoe, towns, backup, ra, beachy, 
    topic=774 level=1 (documents=143): sock, greece, pandesal, butter, peanut, theâ, blackrock, royalties, porsche, payoff, 
    topic=775 level=1 (documents=138): duplicity, breathtaking, theory, 3300, brazilian, academia, rooftop, seat, .slo_hash, ppa, 
    topic=776 level=1 (documents=152): ros, druce, splash, caretaker, empower, feed, initiative, troll, ​slo_hash, prodigiously, 
    topic=777 level=1 (documents=121): crawford, spinco, swindle, deal-, lobster, moving, acre, pa, mooted, built, 
    topic=778 level=1 (documents=124): disinformation, drug, memb, ½í¹í, pounds, ½í¸, nawanno, ashamed, ¼í¿í, ramp, 
    topic=779 level=1 (documents=155): restructure, chest, sunset, die, 84, aka, obtain, organiser, reality, examiner, 
    topic=780 level=1 (documents=148): ahem, socialist, agile, motivation, populist, compared, reports, e, bloke, lecure, 
    topic=781 level=1 (documents=139): politic, rod, lightning, doors, xi, scar, revolving, 54c, insight, smart, 
    topic=782 level=1 (documents=132): â¨, ingredient, inept, capex, colemine, listened, harmful, disgusting, reprehensible, ec, 
    topic=783 level=1 (documents=128): opener, getting, downward, overall, bastards, cumulative, dec14, alumina, genocide, tab, 
    topic=784 level=1 (documents=142): henrique, employes, disruption, physicist, payoff, institute, 69,000, cognitive, aust.slo_cashc, bodes, 
    topic=785 level=1 (documents=113): crazyí, denying, ¾í´ª, claims, speaker, incentive, attach, duplicity, lieberals, jetstar, 
    topic=786 level=1 (documents=135): reopen, lets, spike, refund, juggernaut, slo_hash’sshelters, landscape, treaty, perceive, agendum, 
    topic=787 level=1 (documents=125): dub, resemble, alinta, srsly, violator, place, stifle, schnitzel, ability, inaction, 
    topic=788 level=1 (documents=134): barking, neolib, phon, 43, goner, riddance, wanna, centigrade, birdsville, thar, 
    topic=789 level=1 (documents=121): disgrace, charlie, galloper, â, appro, cray, deli, toy, gallopers, mmmm, 
    topic=790 level=1 (documents=127): guess, gvt, sue, abbott, pharmaceutical, refresh, memory, esso, hedges, upto, 
    topic=791 level=1 (documents=141): thailand, hepburn, coding, guarantee, wedge, heap, kgp, susan, minute, friends/, 
    topic=792 level=1 (documents=116): discuss, echidna, inqld, zcars, potentialco2bomb, vtec, dal, roadshow, complaing, killer, 
    topic=793 level=1 (documents=97): assertion, backseat, driver, soil, gw, w, ahahaha, 53.5, minimise, only17, 
    topic=794 level=1 (documents=83): topknot, landscape, rebellion, boron, pigeon, 22, california, threshold, g., alot, 
    topic=795 level=1 (documents=89): smart, took, decade, basically, voice.willagain, shell, mx, raceway, chartâ, pattern, 
    topic=796 level=1 (documents=66): germany, regulation, gorgeous, chile, concoct, mines"slo_hash, crow, bigger, ret, overtake, 
    topic=797 level=1 (documents=30): etf, 9/11, preparation, nurses, terrific, feasibility, monetary, ijp, guilt, greatest, 
    topic=798 level=1 (documents=36): happened, dumbing, grown, nicest, landslide, biodegradable, organic, hydrocarbon, dolphin, lag, 
    topic=799 level=1 (documents=10): obese, pat, umbrage, amendment, begin, millionaire, morbidly, applaud, dodson, consensus, 
    topic=800 level=1 (documents=14): wind, desal, whitehavenbeach, cancelling, journey, development",says, developments, developmentâ, develops, deverell, 
    topic=801 level=1 (documents=10): waffle, clinch, recite, anonymous, ross, zero, turnbulls, beware, baldwin, anik, 
    topic=802 level=1 (documents=7): relentlessly, loool, andre, 50yrs, punish, sieve, ₹slo_year, developments, developmentâ, develops, 


Process finished with exit code 137 (interrupted by signal 9: SIGKILL)

- this did not complete successfully.

(run 3)
(below with recursive tree depth of 3 only)

- it failed to finish to completion.

Process finished with exit code 137 (interrupted by signal 9: SIGKILL)
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
Biterm Output:

(run 1)
 Topic coherence ..
Topic 0 | Coherence=-176.49 | Top words= adani coal bhp qld santos job australian labor rio gas
Topic 1 | Coherence=-146.07 | Top words= adani coal need climate australia job queensland new labor build
Topic 2 | Coherence=-124.21 | Top words= adani labor qld coal stop want fund support project need
Topic 3 | Coherence=-135.82 | Top words= adani coal loan point abbot government new slo_cashn turnbull project
Topic 4 | Coherence=-145.06 | Top words= adani australian job want oppose project loan new people govt
Topic 5 | Coherence=-126.36 | Top words= adani reef coal great barrier australia want need australian project
Topic 6 | Coherence=-129.98 | Top words= adani coal stop project australia carmichael labor need fund want
Topic 7 | Coherence=-150.89 | Top words= adani coal carmichael court title native federal queensland fund new
Topic 8 | Coherence=-160.12 | Top words= adani santos water coal stop people land whitehaven want farmer
Topic 9 | Coherence=-165.47 | Top words= santos bhp rio new day tinto nsw water gas project
Topic 10 | Coherence=-124.98 | Top words= santos gas coal nsw project pilliga seam narrabri csg farmer
Topic 11 | Coherence=-145.88 | Top words= coal water qld reef climate project money stop loan public
Topic 12 | Coherence=-142.86 | Top words= adani coal loan fund want rail australia qld line veto
Topic 13 | Coherence=-139.23 | Top words= bhp rio tinto tax australia australian ore iron billiton fortescue
Topic 14 | Coherence=-122.33 | Top words= water adani santos basin great artesian nsw risk support australia
Topic 15 | Coherence=-147.24 | Top words= bhp adani tax pay coal company billiton australia year cut
Topic 16 | Coherence=-150.63 | Top words= adani coal job 000 reef create 10 australian queensland kill
Topic 17 | Coherence=-128.56 | Top words= adani joyce barnaby india money coal taxpayer think rail spend
Topic 18 | Coherence=-176.93 | Top words= adani australia santos tax energy pay year woodside people action
Topic 19 | Coherence=-119.81 | Top words= gas field land barnaby narrabri propose nsw inland near joyce


 Texts & Topics ..
australia > bhp billiton things watch ninemsn    (topic: 13)
nsw govt fast track santos csg project day confirmation contaminate aquifer    (topic: 9)
map qld drought       adani get approval unlimited water 26 million litre day    (topic: 14)
santos sign subaru australia year agreement    (topic: 18)
queensland premier mayor work convince adani ahead       (topic: 14)
pm turnbull request publicly fund subsidy bin    (topic: 12)
1 month image coal concentration 10 find adani spill coal lade water wetland (topic: 3)
carbon capture storage exist call leave fuck grind (topic: 2)
terminal job huge contamination    build new coal increase cyclone frequency    (topic: 1)


Time taken to process dataset: 40567.238966464996 seconds, 676.1206494410833 minutes, 11.268677490684722 hours.


Process finished with exit code 0


###########################################################################################

(run 2)
 Topic coherence ..
Topic 0 | Coherence=-153.96 | Top words= adani coal reef australia tax bhp great energy pay barrier
Topic 1 | Coherence=-175.85 | Top words= santos adani great australia whitehaven basin climate action day want
Topic 2 | Coherence=-141.50 | Top words= santos adani coal gas barnaby joyce project rail fund government
Topic 3 | Coherence=-149.54 | Top words= adani coal fund rail project basin galilee money bank public
Topic 4 | Coherence=-144.03 | Top words= adani coal carmichael fund need bank want india stop power
Topic 5 | Coherence=-150.87 | Top words= adani coal loan time new canavan minister support project matt
Topic 6 | Coherence=-137.41 | Top words= adani coal carmichael job queensland project climate australia qld need
Topic 7 | Coherence=-175.41 | Top words= bhp job adani santos 000 year 10 coal iron billiton
Topic 8 | Coherence=-131.63 | Top words= bhp rio tinto billiton tax ore pay iron australia fortescue
Topic 9 | Coherence=-125.09 | Top words= adani loan labor coal stop want election project shorten support
Topic 10 | Coherence=-155.47 | Top words= adani coal job labor lnp queensland qld want whitehaven fund
Topic 11 | Coherence=-191.38 | Top words= coal rio tinto adani australia energy year india santos woodside
Topic 12 | Coherence=-152.15 | Top words= adani coal job qld water reef support great 000 unlimited
Topic 13 | Coherence=-115.98 | Top words= santos gas nsw water project pilliga narrabri seam csg farmer
Topic 14 | Coherence=-148.41 | Top words= adani coal turnbull government native title govt qld big carmichael
Topic 15 | Coherence=-154.30 | Top words= adani climate coal labor change loan billion australian new dollar
Topic 16 | Coherence=-159.14 | Top words= adani people labor stop federal wo santos group government govt
Topic 17 | Coherence=-139.28 | Top words= adani coal point abbot loan carmichael australian reef great government
Topic 18 | Coherence=-149.31 | Top words= coal adani santos people water stop land gas farmer nsw
Topic 19 | Coherence=-220.89 | Top words= time queensland work plan key continue poll block profit morning


 Texts & Topics ..
usa dark brazilian santos bean 5 pound bag coffee bean direct    (topic: 1)
years corners probably piece dodgy backroom goings politician adani    (topic: 10)
essential view tonight 4 corners slo_timepm digging adani     (topic: 1)
question crime branch mundra gujarat dance word adani corners digging adani    (topic: 12)
bhp confident strength chinese economy     (topic: 8)
       (topic: 0)
jonathan moylan receive good behaviour bond whitehaven hoax       (topic: 1)
major shift language labor adani formal opposition certain (topic: 9)
fight adani step way    (topic: 9)


Time taken to process dataset: 39396.074105501175 seconds, 656.6012350916862 minutes, 10.94335391819477 hours.


Process finished with exit code 0

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