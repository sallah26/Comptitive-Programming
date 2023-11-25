s = "()[})(({{[]}}))]"
br_op = s.count("(")
br_cl = s.count(")")
cr_op = s.count("{")
cr_cl = s.count("}")
ang_op = s.count("[")
ang_cl = s.count("]")
if br_op != br_cl:
    return False
elif cr_op != cr_op:
    return False
elif ang_op != ang_cl:
    return False
else: 
    return True
