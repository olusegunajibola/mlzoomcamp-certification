import pickle
def load_models():
    # model_file = 'model1.bin' # for windows
    model_file = 'model2.bin' # for docker
    dv_file = 'dv.bin'
    #model
    with open(model_file, 'rb') as m_in:
        model = pickle.load(m_in)

    # vectorizer
    with open(dv_file, 'rb') as d_in:
        dv = pickle.load(d_in)

    return model, dv