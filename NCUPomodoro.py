import streamlit as st
import time


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)



class Layout(object):
    def __init__(self):
        self.inputSection = st.container()
        self.ctrlSection = st.container()
        self.col1, self.col2, self.col3 = self.ctrlSection.columns(3)
        self.outputSection = st.container()
        self.colImg, self.colText = self.outputSection.columns(2)
        self.thumbnail = st.image("19.jpg", width = 100)

class Timer(object):
    def start(self, Layout, ts):
        if "time" not in st.session_state or not st.session_state.time == None:
            st.session_state.time = ts
            
        with st.empty():
            while st.session_state.time:
                current_time = "%02d：%02d"%(divmod(st.session_state.time, 60))
                st.header(f"{current_time}")
                time.sleep(1)
                st.session_state.time -= 1
            st.write("Time Up!")
            with Layout.colImg:
                Layout.thumbnail.empty()
                Layout.thumbnail = st.image("19.jpg", width = 100)

def main():
    layout = Layout()
    watch = Timer()
    
    with layout.inputSection:
        st.title("NCU蕃茄鐘")
        timer_length = int(st.number_input("輸入倒數時間(以分鐘計)", min_value = 1, value = 25) * 60)

    with layout.ctrlSection:
        with layout.col1:
            start = layout.col1.button("開始倒數")

        with layout.col2:
            stop = layout.col2.button("暫停")
            if stop: pass

        with layout.col3:
            resume = layout.col3.button("繼續")

    with layout.outputSection:
        with layout.colImg:
            if start or resume and "time" in st.session_state:
                layout.thumbnail.empty()
                layout.thumbnail = st.markdown('<video preload="auto" autoplay="autoplay" loop="loop" style="width: 100px; height: 100px;"><source src="https://imgur.com/s6OErOK.mp4" type="video/mp4"></source></video>', unsafe_allow_html=True)

        with layout.colText:
            if start:
                watch.start(layout, timer_length)
            elif resume and "time" in st.session_state:
                watch.start(layout, st.session_state.time)

if __name__ == "__main__":
    main()