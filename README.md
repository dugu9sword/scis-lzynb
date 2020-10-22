# scis-lzynb

## 关于本项目

本库由**牛逼的李宗义**开发，用于将投会议时的 `.bib` 格式文件转化为 SCIS(Science China Information Sciences) 要求的格式（例如，作者名字只保留三个，名字中除了姓保留全拼、其他保留首字母，具体见 https://www.springer.com/journal/11432/submission-guidelines ）：

```tex
% SCIS 的 bib 样例
\begin{thebibliography}{99}

\bibitem{zhang-etal-2019-syntax-infused} Zhang X, Yang Y, Yuan S, et al. Syntax-Infused Variational Autoencoder for Text Generation. In: Proceedings of Annual Meeting of the Association for Computational Linguistics, 2019.

\end{thebibliography}
```

## 使用方法

- 将 `.bib` 文件复制到 `test.bib` 中，注意需要修改一些地方以方便程序处理，如下所示：
```tex
@article{zss1989,
    % 条目内不要有换行！
    author = {Zhang, K. 
    and 
    Shasha, D.},
    title = {Simple Fast Algorithms for the Editing Distance Between Trees and Related Problems},
    journal = {SIAM J. Comput.},
    year = {1989},
    % 条目间不要有空行！

    publisher = {Society for Industrial and Applied Mathematics}
} 
```
- 将**原始**的 `.tex` 文件复制到 `test.tex` 中（根据文章内容进行引用条目筛选）
- 运行 `lzynb.py`，就可以由**牛逼的李宗义**进行引用格式转换了

## 样例
运行项目自带的文档，输出：
```
\bibitem{Feng2012stylish} Feng S, Banerjee R, Choi Y. Characterizing Stylistic Elements in Syntactic Structure. EMNLP and Computational Natural Language Learning, 2012.
\bibitem{Sarawgi2011GenderAT} Sarawgi R, Gajulapalli K, Choi Y. Gender Attribution: Tracing Stylometric Evidence Beyond Topic and Genre. In: Proceedings of Conference on Computational Natural Language Learning, 2011.

% >>>>>> 下面这个会议可能有问题：Raghavan2010author
\bibitem{Raghavan2010author} Raghavan S, Kovashka A, Mooney R. Authorship Attribution Using Probabilistic Context-free Grammars. ACL Short Papers, 2010.
\bibitem{Wong2011native} Wong S, Dras M. Exploiting Parse Structures for Native Language Identification. Proceedings of the Conference on Empirical Methods in Natural Language Processing, 2011.
\bibitem{Kemper1987} Kemper S. {Life-span Changes in Syntactic Complexity}. Journal of Gerontology, 1987.


Found5bibs
```

## 售后
具体咨询李宗义。