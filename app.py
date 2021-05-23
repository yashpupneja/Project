import streamlit as st

#Component Pkgs
import streamlit.components.v1 as components 

import base64

#Pkgs - Files
import Html
import Css
import NLP_NER, NLP_pos, NLP_sentiment

def main():
	
	Css.local_css("style.css")
	Css.side_background()
	choices=["Home", "Applications"]
	choice = st.sidebar.selectbox("Select Activity",choices)

	if choice == 'Home':
		st.markdown(Html.html_heading(), unsafe_allow_html = True)
		st.markdown(Html.html_sub(),unsafe_allow_html=True)
		st.markdown(Html.html_intro(), unsafe_allow_html=True)


	elif choice == 'Applications':
		categories = ['Named Entity Recognition', 'Part-of-Speech Tagging', 'Sentiment Detection']
		apps_nlp = st.sidebar.radio("Pick a Domain",categories)
		if apps_nlp == 'Named Entity Recognition':
			NLP_NER.main()

		elif apps_nlp == 'Part-of-Speech Tagging':
			NLP_pos.main()

		elif apps_nlp == 'Sentiment Detection':
			NLP_sentiment.add_flair()


if __name__ == '__main__':
	main()
