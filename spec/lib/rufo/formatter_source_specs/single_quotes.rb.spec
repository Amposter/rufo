#~# ORIGINAL
#~# quote_style: :single

"a great string"

#~# EXPECTED

'a great string'

#~# ORIGINAL
#~# quote_style: :single

"🚀"

#~# EXPECTED

'🚀'

#~# ORIGINAL
#~# quote_style: :single

""

#~# EXPECTED

''

#~# ORIGINAL
#~# quote_style: :single

"it's ok"

#~# EXPECTED

"it's ok"

#~# ORIGINAL
#~# quote_style: :single

"#{interpolation}"

#~# EXPECTED

"#{interpolation}"

#~# ORIGINAL
#~# quote_style: :single

"\0 \x7e \e \n \r \t \u1f680 \'"

#~# EXPECTED

"\0 \x7e \e \n \r \t \u1f680 \'"

#~# ORIGINAL
#~# quote_style: :single

%q(single)

#~# EXPECTED

%q(single)

#~# ORIGINAL
#~# quote_style: :single

%Q(double)

#~# EXPECTED

%Q(double)
