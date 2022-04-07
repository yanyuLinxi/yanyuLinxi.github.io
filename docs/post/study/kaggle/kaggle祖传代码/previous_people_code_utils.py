#

# 归一化

def norm_fit(df_1, saveM=True, sc_name='quan'):
    # 进行归一化。对每一列尽心归一化。既然这样我们先不用高斯归一化，先用它这个归一化。这个函数写的很好，我们直接用可以。
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
    ss_1_dic = {
        'zsco': StandardScaler(),
        'mima': MinMaxScaler(),
        'maxb': MaxAbsScaler(),
        'robu': RobustScaler(),
        'norm': Normalizer(),
        'quan': QuantileTransformer(n_quantiles=100, random_state=0, output_distribution="normal"),
        'powe': PowerTransformer()
    }
    ss_1 = ss_1_dic[sc_name]
    df_2 = pd.DataFrame(ss_1.fit_transform(df_1), index=df_1.index, columns=df_1.columns)
    if saveM == False:
        return (df_2)
    else:
        return (df_2, ss_1)

# 归一化transform
def norm_tra(df_1, ss_x):
    # transform_data
    df_2 = pd.DataFrame(ss_x.transform(df_1), index=df_1.index, columns=df_1.columns)
    return (df_2)

# seed everything
def seed_everything(seed=2019):
    # 哈哈哈，这个函数好啊，我们mark了。我非常喜欢。
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True

# pytorch 训练框架

def train_fn(model, optimizer, scheduler, loss_fn, dataloader, device):
    # 将模型常用的train等方法提取出来十分的好用好像。可以避免杂乱无章的代码。
    model.train()
    final_loss = 0
    scores = 0

    for data in dataloader:
        optimizer.zero_grad()
        inputs, targets = tuple(t.to(device) for t in data)
        outputs = model(inputs)
        outputs = F.softmax(outputs, dim=1)
        loss = loss_fn(outputs, targets)
        loss.backward()
        optimizer.step()
        scheduler.step()

        final_loss += loss.item()
        score = utils.evaluate_only_scores(targets.cpu(), outputs[:, 1].cpu().detach().numpy())
        scores += score

    final_loss /= len(dataloader)
    scores /= len(dataloader)

    return final_loss, scores


def valid_fn(model, loss_fn, dataloader, device):
    model.eval()
    final_loss = 0
    scores = 0
    valid_preds = []

    for data in dataloader:
        inputs, targets = tuple(t.to(device) for t in data)
        outputs = model(inputs)
        outputs = F.softmax(outputs, dim=1)
        loss = loss_fn(outputs, targets)
        final_loss += loss.item()
        valid_preds.append(outputs[:, 1].detach().cpu().numpy())

        score = utils.evaluate_only_scores(targets.cpu(), outputs[:, 1].cpu().detach().numpy())
        scores += score


    final_loss /= len(dataloader)
    scores /= len(dataloader)
    valid_preds = np.concatenate(valid_preds)

    return final_loss, scores, valid_preds


def inference_fn(model, dataloader, device):
    model.eval()
    preds = []

    for data in dataloader:
        inputs = data['x'].to(device)
        with torch.no_grad():
            outputs = model(inputs)

        preds.append(outputs.sigmoid().detach().cpu().numpy())

    preds = np.concatenate(preds)

    return preds