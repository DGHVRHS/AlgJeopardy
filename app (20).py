import streamlit as st

st.set_page_config(page_title="Jeopardy!", layout="wide")

# Game Data (4 Categories: Substitution, Elimination, Did it happen?, Netflix Hits)
JEOPARDY_DATA = {
    "Substitution Method": [
        {
            "val": 200,
            "q": r"Solve the system using substitution: $\begin{cases} 2x + 3y = 19 \\ y = 3x - 1 \end{cases}$",
            "a": r"$(2, 5)$  \n  *($2x + 3(3x - 1) = 19 \implies 11x = 22 \implies x = 2, y = 5$)*"
        },
        {
            "val": 400,
            "q": r"Solve the system using substitution: $\begin{cases} x - 3y = 4 \\ 2x + 5y = 30 \end{cases}$",
            "a": r"$(10, 2)$  \n  *($x = 3y + 4 \implies 2(3y + 4) + 5y = 30 \implies 11y = 22 \implies y = 2, x = 10$)*"
        },
        {
            "val": 600,
            "q": r"A baker uses $2$ cups of sugar per batch of cookies ($c$) and $4$ cups per cake ($k$), using $36$ cups total. If she made $3$ more batches of cookies than cakes ($c = k + 3$), how many of each did she make?",
            "a": r"$8$ batches of cookies and $5$ cakes  \n  *($2(k + 3) + 4k = 36 \implies 6k = 30 \implies k = 5, c = 8$)*"
        },
        {
            "val": 800,
            "q": r"Maya bought $2$ binders ($b$) and $5$ pens ($p$) for $\$13.50$. At this store, $1$ binder costs the same as $2$ pens ($b = 2p$). Find the cost of one binder and one pen.",
            "a": r"Binder: $\$3.00$, Pen: $\$1.50$  \n  *($2(2p) + 5p = 13.50 \implies 9p = 13.50 \implies p = 1.50, b = 3.00$)*"
        },
        {
            "val": 1000,
            "q": r"Solve the system using substitution and state the number of solutions: $\begin{cases} y = -2x + 7 \\ 6x + 3y = 15 \end{cases}$",
            "a": r"No solution (parallel lines)  \n  *($6x + 3(-2x + 7) = 15 \implies 21 = 15$, which is false)*"
        }
    ],
    "Elimination Method": [
        {
            "val": 200,
            "q": r"Solve the system using elimination: $\begin{cases} 5x + 3y = 30 \\ -5x + 4y = 5 \end{cases}$",
            "a": r"$(3, 5)$  \n  *(Adding equations gives $7y = 35 \implies y = 5, x = 3$)*"
        },
        {
            "val": 400,
            "q": r"Solve the system using elimination: $\begin{cases} 4x + 3y = 24 \\ 4x - 2y = 4 \end{cases}$",
            "a": r"$(3, 4)$  \n  *(Subtracting equations gives $5y = 20 \implies y = 4, x = 3$)*"
        },
        {
            "val": 600,
            "q": r"Solve the system using elimination: $\begin{cases} 3x + 2y = 23 \\ 6x - 5y = 10 \end{cases}$",
            "a": r"$(5, 4)$  \n  *(Multiply top equation by $-2$ to eliminate $x$: $-9y = -36 \implies y = 4, x = 5$)*"
        },
        {
            "val": 800,
            "q": r"Solve the system using elimination: $\begin{cases} 3x + 5y = 22 \\ 2x - 3y = 2 \end{cases}$",
            "a": r"$(4, 2)$  \n  *(Multiply top by $3$ and bottom by $5$: $19x = 76 \implies x = 4, y = 2$)*"
        },
        {
            "val": 1000,
            "q": r"At a concession stand, $3$ hot dogs ($h$) and $2$ sodas ($s$) cost $\$13.00$, while $4$ hot dogs and $5$ sodas cost $\$22.00$. Find the cost of one hot dog and one soda.",
            "a": r"Hot dog: $\$3.00$, Soda: $\$2.00$  \n  *($3h + 2s = 13$ and $4h + 5s = 22 \implies 7h = 21 \implies h = 3, s = 2$)*"
        }
    ],
    "Did it happen?": [
        {
            "val": 200,
            "q": "Did it happen? In March 2021, a massive container ship named the Ever Given got stuck sideways in the Suez Canal for six days, blocking billions of dollars in global trade.",
            "a": "YES, it happened! (March 23–29, 2021)"
        },
        {
            "val": 400,
            "q": "Did it happen? In 2019, NASA successfully landed the first human astronauts on Mars as part of the Artemis I mission.",
            "a": "NO, it did not happen! (Artemis I was an uncrewed Moon mission in 2022; no human has walked on Mars.)"
        },
        {
            "val": 600,
            "q": "Did it happen? At the 2017 Oscars, 'La La Land' was mistakenly announced as the Best Picture winner before the real winner, 'Moonlight', was called to the stage.",
            "a": "YES, it happened! (89th Academy Awards, February 2017)"
        },
        {
            "val": 800,
            "q": "Did it happen? In 2020, Australia passed an emergency law banning the sale of all physical books nationwide for three months to prevent paper shortages.",
            "a": "NO, it did not happen! (Bookstores remained open or operated online throughout 2020.)"
        },
        {
            "val": 1000,
            "q": "Did it happen? In 2023, the Louvre Museum in Paris closed for a week after wild boars broke into a basement gallery and damaged three Renaissance paintings.",
            "a": "NO, it did not happen! (Complete fabrication.)"
        }
    ],
    "Netflix Hits": [
        {
            "val": 200,
            "q": "Set in the 1980s in Hawkins, Indiana, this sci-fi horror hit follows a group of kids searching for their missing friend Will and encountering a girl with psychokinetic powers named Eleven.",
            "a": "Stranger Things"
        },
        {
            "val": 400,
            "q": "This 2021 South Korean survival drama became Netflix's most-watched series of all time, featuring 456 debt-ridden contestants competing in deadly versions of children's games.",
            "a": "Squid Game"
        },
        {
            "val": 600,
            "q": "Released in 2022 and starring Jenna Ortega, this supernatural comedy-horror series follows the Addams Family daughter as she attends Nevermore Academy.",
            "a": "Wednesday"
        },
        {
            "val": 800,
            "q": "Based on Julia Quinn's romance novels and produced by Shonda Rhimes, this Regency-era period drama follows the eight close-knit siblings of a wealthy London family.",
            "a": "Bridgerton"
        },
        {
            "val": 1000,
            "q": "Starring Anya Taylor-Joy as chess prodigy Beth Harmon, this 2020 miniseries sparked a massive global surge in chess set sales.",
            "a": "The Queen's Gambit"
        }
    ]
}

# Session State Setup for 4 Teams
if "scores" not in st.session_state:
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
if "used_questions" not in st.session_state:
    st.session_state.used_questions = set()
if "active_q" not in st.session_state:
    st.session_state.active_q = None

st.title("🏆 Classroom Jeopardy!")

# Scoreboard Sidebar
st.sidebar.header("Scoreboard")
for team in st.session_state.scores:
    st.session_state.scores[team] = st.sidebar.number_input(
        f"{team}", value=st.session_state.scores[team], step=100
    )

if st.sidebar.button("Reset Game"):
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
    st.session_state.used_questions = set()
    st.session_state.active_q = None
    st.rerun()

# Active Question Screen
if st.session_state.active_q:
    q_data = st.session_state.active_q
    st.info(f"**Category:** {q_data['cat']} | **Value:** ${q_data['val']}")
    
    st.markdown(f"### {q_data['q']}")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Answer"):
            st.success(f"**Answer:** {q_data['a']}")
    
    st.write("### Award Points:")
    score_cols = st.columns(4)
    for idx, team in enumerate(st.session_state.scores):
        if score_cols[idx].button(f"+${q_data['val']} to {team}"):
            st.session_state.scores[team] += q_data['val']
            st.session_state.active_q = None
            st.rerun()
            
    if st.button("Close Question without Points"):
        st.session_state.active_q = None
        st.rerun()

else:
    # 4-Column Jeopardy Grid
    categories = list(JEOPARDY_DATA.keys())
    cols = st.columns(len(categories))

    for cat_idx, cat in enumerate(categories):
        with cols[cat_idx]:
            st.markdown(f"### {cat}")
            for q_idx, item in enumerate(JEOPARDY_DATA[cat]):
                q_id = f"{cat}_{q_idx}"
                if q_id in st.session_state.used_questions:
                    st.button("---", key=q_id, disabled=True, use_container_width=True)
                else:
                    if st.button(f"${item['val']}", key=q_id, use_container_width=True):
                        st.session_state.used_questions.add(q_id)
                        st.session_state.active_q = {**item, "cat": cat}
                        st.rerun()
