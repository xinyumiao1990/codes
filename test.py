def checkbrace(input_str):
  stack = []
  for s in input_str:
    if s=="(":
      stack.append(s)
    if s == ")":
      if len(stack) > 0:
        stack.pop()
      else:
        return False
        
  if len(stack) == 0:
    return True
  else:
    return False
    
def binarysearch(input_list, elem):
  left = 0
  right = len(input_list) - 1
  found = False
  while left <= right and not found:
    middle  = (left + right)//2
    if input_list[middle] > elem:
      right = middle - 1
    elif input_list[middle] == elem:
      found = True
    else:
      left = middle + 1
  return found
      
    
print checkbrace("()()")

print binarysearch(['a','b','c','d','e','h'], 'h')


#sigfig:

# Write a function to perform run-length encoding. E.g. convert aaaabbcccaeeeee => a4b2c3ae5.


def strCompress(input_str):
    if len(input_str) == 0:
        return ""
    
    result = ""
    counter = 0
    prev_ch = None
    
    for ch in input_str:
        curr_ch = ch
        if prev_ch is None or curr_ch == prev_ch:
            counter += 1
        elif curr_ch != prev_ch:
            if counter == 1:
                result += prev_ch
            else:
                result += prev_ch + str(counter)
            counter = 1
        prev_ch = curr_ch
    
    if counter == 1:
        result += prev_ch
    else:
        result += prev_ch + str(counter)
    return result

print strCompress("aaaaaaee")
        
             









#primer:


import json

docid_to_title = json.loads('{"28099931907": {"content": {"title": "Zika dollars and Internet fight in play as government shutdown looms"}}, "28108959337": {"content": {"title": "Leaders express renewed optimism about flood relief as Congress aims to avoid a government shutdown"}}, "28110814722": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28101422554": {"content": {"title": "Senate blocks bill to avert shutdown as De..."}}, "28099132063": {"content": {"title": "Senate Dems threaten shutdown over Flint aid"}}, "28101167069": {"content": {"title": "Zika dollars, internet fight in play as government shutdown looms"}}, "28102817621": {"content": {"title": "House leaders reach deal on Flint aid, potentially averting shutdown"}}, "28108039075": {"content": {"title": "Deal reached to keep US government running, help Flint"}}, "28098698025": {"content": {"title": "Defeat of Republicans\\u2019 stop-gap spending bill brings federal government closer to a shutdown"}}, "28097027782": {"content": {"title": "Will Democrats force a government shutdown over Flint relief funds?"}}, "28111131355": {"content": {"title": "Lawmakers strike deal to avoid shutdown"}}, "28110856451": {"content": {"title": "Louisiana flood aid, $500 million, survives Senate budget fight"}}, "28106625838": {"content": {"title": "Pelosi aide says deal with Speaker Ryan covers Flint aid"}}, "28099931906": {"content": {"title": "Zika dollars  and Internet fight in play as government shutdown  looms"}}, "28096859458": {"content": {"title": "Are Democrats pushing the federal government toward a shutdown?"}}, "28110814723": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28093906031": {"content": {"title": "will democrats force a federal shutdown over Flint relief funds?"}}, "28108873175": {"content": {"title": "Senate Democrats accept deal on Flint aid, potentially averting shutdown"}}, "28103573587": {"content": {"title": "ALEXANDER : Senate Democrats\\u2019 Election Politics Are Putting Babies at Risk"}}, "28096849799": {"content": {"title": "Democrats poised to block stopgap funding bill over Flint"}}, "28098943696": {"content": {"title": "Senate blocks stopgap bill to prevent shutdown this weekend"}}, "28110942840": {"content": {"title": "Senate Passes Short-Term Government Funding Measure"}}, "28107038234": {"content": {"title": "House aides: Deal reached to help Flint, keep US gov\'t open"}}, "28084509076": {"content": {"title": "Week ahead: Spending fight shifts from Zika to Flint"}}, "28089633072": {"content": {"title": "Flint water aid spending bill\'s sticking point"}}, "28099749478": {"content": {"title": "Government shutdown looms due to partisan clash over Flint aid"}}, "28099468922": {"content": {"title": "Funding bill rejected as shutdown nears"}}, "28107540657": {"content": null}, "28098940419": {"content": {"title": ""}}, "28110838282": {"content": {"title": "Senate approves deal to keep government open, combat Zika"}}, "28093943889": {"content": {"title": "Democrats press talks as showdown vote looms on funding bill"}}, "28099506681": {"content": {"title": "Republicans ready new bid to avoid shutdown"}}, "28084188573": {"content": {"title": "Zika: Congressional showdown coming this week"}}, "28109130960": {"content": {"title": "McConnell: Let\\u2019s Keep Working Together to Pass Critical Resources"}}, "28097129455": {"content": {"title": "McConnell: We Cannot Afford to Wait Any Longer on Providing Critical Resources"}}, "28110653655": {"content": {"title": "Deal averts federal shutdown, ignores Cruz\' Internet \'giveaway\'"}}, "28110819318": {"content": {"title": "Senate passes spending bill after separate Flint aid deal"}}, "28106754872": {"content": {"title": "Democrats: Deal reached to help Flint, keep US gov\'t open"}}, "28093906030": {"content": {"title": "Will Democrats force a federal shutdown over Flint relief funds?"}}, "28108257314": {"content": {"title": "US Senate Again Blocks Bill That Includes Zika Funding"}}, "28097690131": {"content": {"title": "Cornyn: Democrats Pushing Country Towards Shutdown for Political Gain"}}, "28096854777": {"content": {"title": "Flint aid at center of funding standoff in Congress"}}, "28100917473": {"content": {"title": "A government shutdown is looming because of a clash over aid for Flint, Michigan"}}, "28099198548": {"content": {"title": "Senate Dems block gov\'t funding bill over Flint aid"}}, "28110814724": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28110749186": {"content": {"title": "Senate advances bill to avert government shutdown after Flint deal struck"}}, "28110001860": {"content": {"title": "Congress set to avert government shutdown, offer Zika relief"}}, "28109184578": {"content": {"title": "Deal reached to keep U.S. government running, help Flint"}}, "28100566138": {"content": {"title": "Democrats poised to block stopgap funding bill over Flint"}}, "28085937302": {"content": {"title": "FOUR DAYS UNTIL NEXT REPUBLICAN GOVERNMENT SHUTDOWN"}}, "28108954857": {"content": {"title": "Congress nears deal to keep government open"}}, "28098853699": {"content": {"title": "Senate Democrats Block Republican Stopgap From Advancing"}}, "28110991149": {"content": {"title": "Senate passes bill to avoid government shutdown"}}, "28098130400": {"content": {"title": "Congress weighs plan to dodge shutdown"}}}')

# 1. Write a function that identifies all the unique words across all the `content.title` fields in `docid_to_title`.
result1 = set([])
for doc in docid_to_title.keys():
    record = docid_to_title[doc]
    if record.get("content") is None:
        continue
    if record["content"].get("title") is None:
        continue
    worklist = record["content"]["title"].split(" ")
    for w in worklist:
        result1.add(w)
#print result1

# 2. Write a function that computes the k most frequent bigrams across all the `content.title` fields in `docid_to_title`.
result2 = {}
for doc in docid_to_title.keys():
    record = docid_to_title[doc]
    if record.get("content") is None:
        continue
    if record["content"].get("title") is None:
        continue
    worklist = record["content"]["title"].split(" ")
    for i in xrange(len(worklist)):
        if i >= len(worklist) - 1:
            break
        bigrams = worklist[i]+' ' +worklist[i+1] 
        if result2.get(bigrams) is None:
            result2[bigrams] = 1
        else:
            result2[bigrams] += 1

print [result2.get(c) for c in sorted(result2, key=result2.get, reverse=True)[:5]]
            



# 3. Find all the duplicate titles in `content.title` fields in `docid_to_title`.
s = set([])
result3 = set([])
for doc in docid_to_title.keys():
    record = docid_to_title[doc]
    if record.get("content") is None:
        continue
    if record["content"].get("title") is None:
        continue
    current_title = record["content"]["title"].lower()
    if current_title in s:
        result3.add(current_title)
    else:
        s.add(current_title)
print result3




# Write a function that given two arrays, will return the intersection of those arrays. E.g. Given [1, 2, 3, 4, 5] and [6, 3, 5, 2, 7], it should return [2, 3, 5].

# return an array of unique values
# input are all integers

# def intersection(arr1, arr2):
#     if len(arr1) == 0 or len(arr2) == 0:
#         return []
#     s = set([])
#     result = []
#     temp = set([])
#     for elem in arr2:
#         s.add(elem)
#     for elem in arr1:
#         if elem in s:
#             if elem not in temp:
#                 result.append(elem)
#                 temp.add(temp)
#     return result

# [1, 2, 3, 4], [2, 4] => [2, 4]  x [4, 2]
