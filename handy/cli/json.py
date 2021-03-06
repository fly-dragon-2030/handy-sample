import sys

from handy.jzon.handler import load,save
from handy.dict.mixedict import delkey, findkey, isin, rmempty, replkey
from ._constants import msg_file_not_found

msg_help_chkey = "Written by junying, 2019-04-29 \
                 \nComment: to check if the query key exists or not in the file.\
                 \nUsage: chkey [keyname] [inpath]"
def chKey():
    if len(sys.argv) < 3: print(msg_help_chkey); return
    try: indata = load(sys.argv[2])
    except: return "No JSON object could be decoded"
    if not indata: print(msg_file_not_found); return
    if not isin(indata,sys.argv[1]): print("no found!")
    else: print("found!!!")
    
msg_help_delkey = "Written by junying, 2019-04-29 \
                  \nComment: to delete a specific key in a json file.\
                  \nUsage: delkey [key] [inpath] [outpath]"

from ._constants import msg_no_output, yes_symbols, no_symbols,print_symbols

def delKey():
    if len(sys.argv) < 3: print(msg_help_delkey); return
    elif len(sys.argv) == 3:
        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
        if not answer or any(symbol in answer[0] for symbol in yes_symbols): outpath=sys.argv[2]
        elif any(symbol in answer[0] for symbol in no_symbols): return
        else: outpath = answer
    else: outpath = sys.argv[3]
    try: indata = load(sys.argv[2]); key = sys.argv[1]
    except: return "No JSON object could be decoded"
    if not indata: print(msg_file_not_found); return
    delkey(indata,key); rmempty(indata); save(indata,outpath)

msg_help_findkey = "Written by junying, 2019-05-09 \
                   \nComment: return the value of a specific key in a json file.\
                   \nUsage: findkey [keyname] [inpath]"
def findKey():
    if len(sys.argv) < 3: print(msg_help_findkey); return
    try: indata = load(sys.argv[2])
    except: return "No JSON object could be decoded"
    if not indata: print(msg_file_not_found); return
    if not isin(indata,sys.argv[1]): print("no found!")
    else:
        for value in findkey(indata,sys.argv[1]): print(value)
    
msg_help_rmempty = "Written by junying, 2019-04-29 \
                   \nComment: remove keys with the empty values. \
                              and to humanize it.\
                   \nUsage: rmempty [inpath] [outpath]"
            
def rmEmpty():
    if len(sys.argv) < 2: print(msg_help_rmempty); return
    elif len(sys.argv) == 2:
        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
        if not answer or any(symbol in answer[0] for symbol in yes_symbols): outpath=sys.argv[1]
        elif any(symbol in answer[0] for symbol in no_symbols): return
        else: outpath = answer
    else: outpath = sys.argv[2]
    # load
    try: indata = load(sys.argv[1])
    except: return "No JSON object could be decoded"
    if not indata: print(msg_file_not_found); return
    # process
    rmempty(indata)
    # save
    save(indata,outpath)

msg_help_replkey = "Written by junying, 2019-08-05 \
                   \nComment: replace the value of a specific key from A to B.\
                   \nUsage: replkey [key] [value] [inpath]"
                 
def replKey():
    if len(sys.argv) < 4: print(msg_help_replkey); return
    elif len(sys.argv) == 4:
        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
        if not answer or any(symbol in answer[0] for symbol in yes_symbols): outpath=sys.argv[3]
        elif any(symbol in answer[0] for symbol in no_symbols): return
        else: outpath = answer
    else: outpath = sys.argv[4]
    # load
    try: indata = load(sys.argv[3])
    except: return "No JSON object could be decoded"
    if not indata: print(msg_file_not_found); return
    # process
    replkey(indata,sys.argv[1],sys.argv[2])
    # save
    if any(symbol in answer[0] for symbol in print_symbols): print(indata); return
    else: save(indata,outpath)