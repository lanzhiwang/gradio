with gr.Blocks() as demo:
    with gr.Row():
        gr.Image("lion.jpg", scale=2)
        gr.Image("tiger.jpg", scale=1)
demo.launch()