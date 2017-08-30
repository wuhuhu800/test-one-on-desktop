fromatter = "%r %r %r %r"

print fromatter %(1,2,3,4)
print fromatter %("one","two","three","four",)
print fromatter %(True,False,False,True)
print fromatter %(fromatter,fromatter,fromatter,fromatter)
print fromatter %(
      "I had this thing.",
      "That you could type up right.",
      "But it didn't sing.",
      "So I said goodnight."
      )
      