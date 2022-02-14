export const variantsIni = `
# Hybrid of antichess and atomic.
[antiatomic:giveaway]
blastOnCapture = true

# Hybrid of atomic and zh. Zh is th base variant.
[atomiczh:atomic]
pieceDrops = true
capturesToHand = true
pocketSize = 6
castling = false

[epicatomic:atomic]
variantTemplate = atomic
king = k
queen = q
bishop = b
knight = n
rook = r
pawn = p
promotionPieceTypes = bn
blastOnCapture = true
castling = false
startFen = 10/rnbqknnbnr/pppppppppp/10/10/10/10/PPPPPPPPPP/RNBQKNNBNR/10[] w - - 0 1
maxRank = 10
maxFile = 10
chess960 = false
promotionRank = 8
doubleStep = false
castling = false

[atomicrk:atomic]
startFen = 8/8/8/8/8/8/krbnNBRK/qrbnNBRQ w - - 0 1
flagPiece = k
whiteFlag = *8
flagMove = true
castling = false
checking = false`
