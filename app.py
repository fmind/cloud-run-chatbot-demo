import gradio as gr

def demo(message, history):
    return message

gr.ChatInterface(demo).launch()