import torch
from torch import nn


class EncoderDecoder(nn.Module):
    def __init__(self, encoder, decoder):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x , captions):
        enc_outputs = self.encoder(x)
        dec_outputs = self.decoder(enc_outputs, captions)
        return dec_outputs


