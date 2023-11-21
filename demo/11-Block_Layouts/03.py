with gr.Blocks() as demo:
    with gr.Tab("Lion"):
        gr.Image("lion.jpg")
        gr.Button("New Lion")
    with gr.Tab("Tiger"):
        gr.Image("tiger.jpg")
        gr.Button("New Tiger")
