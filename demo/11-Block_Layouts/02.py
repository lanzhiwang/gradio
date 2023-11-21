with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            text1 = gr.Textbox()
            text2 = gr.Textbox()
        with gr.Column(scale=4):
            btn1 = gr.Button("Button 1")
            btn2 = gr.Button("Button 2")
