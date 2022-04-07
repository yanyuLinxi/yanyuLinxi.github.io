---
title: "Spark学习计划"
date: 2022-01-04T09:43:28+08:00
tags : [
   "spark"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

spark学习计划：https://zhuanlan.zhihu.com/p/384903354
Scala学习《Scala实用指南》
然后书籍路线，我目前自己的学习路线是：《Spark权威指南》->《Spark内核设计的艺术 架构设计与实现》->《SparkSQL内核剖析》，也就是先从第一本API表层原理的入门书开始

学习spark2。然后到时候转spark3。先做到会用。
https://blog.csdn.net/chengyuqiang/category_9270040.html

spark中文教程
https://spark-reference-doc-cn.readthedocs.io/zh_CN/latest/deploy-guide/cluster-overview.html

# spark生产环境开发环境远程开发环境搭建
https://zhuanlan.zhihu.com/p/55450219

https://cloud.tencent.com/developer/article/1482700
https://blog.csdn.net/lijingjingchn/article/details/83143093
https://developer.aliyun.com/article/108549


# 教程
可能还不错的：
https://sparkbyexamples.com/


# 速看视频随记
1. 集群模式，主从模式，一个控制端，几个从属端。可以在一个机子上部署。主从之间通过端口7077进行通信。
   1. 高可用模式，建立备用的master。当主要的master断开之后，后续的master会顶替上来。
2. yarn模式。
3. 主要运行模式：编写脚本然后提交运行。

# RDD
1. RDD体现了装饰者的设计模式，所有的操作在前面的RDD上进行封装。
   1. 装饰者模式，允许向现有对象上添加新的功能，同时不改变其结构。将现有类进行包装。
2. RDD是一个抽象类，代表弹性、不可变、可分区、里面元素可并行计算的集和
   1. 弹性：
      1. 存储的弹性：内存、与磁盘的自动切换：内存有限制。所以内存不能装入所有的数据。RDD支持数据在内存和磁盘的自动切换。对上层透明。
      2. 容错的弹性：数据丢失可以自动恢复：数据丢失了，可以重新读取数据。
      3. 计算的弹性：计算出错重试机制。计算出错后，可以重新计算。容错机制。
      4. 分区的弹性：可根据需要重新分片。根据计算资源的需要重新分区。
3. RDD特性：
   1. 分布式：数据存储在大数据集群不同节点上。对上层透明。
   2. 数据抽象（数据集）：只封装了计算逻辑，并不保存数据。需要子类实现计算逻辑。
   3. 不可变。RDD不可以改变，想要改变只能生成新的RDD。在新RDD里封装计算逻辑。
   4. 可分区，可并行计算：
   5. 惰性计算。只有在真正需要的时候，才会执行业务逻辑。
4. 五大属性
   1. 分区列表。多个分区用来执行并行计算。getPartitions函数
   2. 分区逻辑函数：每个分区的计算逻辑。每个分区的计算逻辑相同。computing函数
   3. RDD依赖关系：一个依赖于其他RDD依赖的列表。getDependencies获取依赖。
   4. 分区器partitioner。可选的。数据如何分区
   5. 首选位置prefer location。可选的。判断计算发送到哪个节点效率最优（计算和数据在同一个集群效率更优）
5. RDD的作用
   1. 进行逻辑的封装，并生成Task，发送给Executor节点。
6. RDD分区和并行度
   1. RDD根据分区来生成Task。
      1. 在行动算子触发Task后，是将一个Task所有的逻辑执行完毕后，再执行下一个Task的。
      2. 同一分区内执行顺序是有序的。不同分区执行是无序的（并行的）
   2. 根据Task和Executor的数量来影响并行度。


# Spark执行原理

1. Spark执行
   1. 申请资源。
   2. 将数据处理逻辑，分成一个一个的计算任务。
   3. 将任务分配到资源的计算节点上。
2. 以Yarn为例的工作原理
   1. 启动Yarn集群环境。资源管理器ResourceManager和若干个节点管理器NodeManager。
   2. Spark申请资源创建调度节点Driver和计算节点Executor。
   3. Driver将计算逻辑根据**分区**划分成不同的任务Task，并将Task组成TaskPool。
      1. Driver主要来做调度。
   4. Driver根据计算节点的状态将TaskPool中的Task发送到对应的计算节点进行计算。

# Spark 代码
1. 准备环境
   1. 基础登录设置
   2. val sparkConf = new SparkConf().setMaster("local").setAppName("") # 设置本地环境。
      1. "local"单线程单核。local[*]多线程模拟多集群。
   3. val sc = new SparkContext(sparkConf)
2. 关闭环境：sc.stop()
3. RDD相关
   1. RDD的内部方法将计算逻辑发送到Executor端进行执行。所以将RDD方法称为算子。
   2. RDD创建
      1. 从内存创建
         1. **sc.parallelize**(data=数据集合, numSlices=Option[n])
            1. parallelize意思是并行。
            2. numSlices表示分区的数量。可以缺省。缺省的话即使用默认的并行度defaultParallelism。
               1. defaultParallelism默认值来自scheduler.conf.getInt("spark.default.parallelism", totalCores)
               2. 默认情况下，从配置对象conf中获取配置参数spark.default.parallelism
               3. 如果取不到，会因为设置为local[*]为当前环境的最大可用核数。
               4. 当**numSlices不可以整分**的时候。通过读源码可以看到。不是均匀划分。是依次划分。
         2. **sc.makeRDD**(数据集合) 调用同parallelize函数。
            1. 这个函数实现时调用了parallelize函数。
      2. 从文件中创建。
         1. **sc.textFile**(path="",minPartitions)。以行为单位读取数据
            1. path可以是文件名、可以是目录名
            2. path以当前环境的根路径为基准（项目路径）。可以写绝对路径。也可以写相对路径。
            3. path中可以使用通配符 path="dataste/1*.txt"
            4. minPartitions为最小的分区数量=math.min(defaultParallelism, 2)。在默认最小分区下，可以往上增加分区，同下。
            5. 如果不使用默认的分区数量，可以指定。spark读取文件，底层使用的hadoop的方式，统计字节数（注意换行算一个字节），字节数除以分区数，得到一个余数，如果余数大于百分之十，则加一个分区，否则就不加分区。
               1. 例子：7个字节，分两个分区。7（字节）/2（分区）=3（字节/分区）。7/3（字节/分区）=2...1分区。余出来的分区书来给你超过了百分之10，加一个分区。
               2. 总结。以文件字节数为单位统计分区。以行为单位读取文件并存入分区。
         2. **sc.wholeTextFiles** 以文件为单位读取文件。会显示数据来源。
   3. RDD存储
      1. **saveAsTextFile**(path)
         1. 存成文本文件。
   4. RDD逻辑相关方法：RDD算子（解决问题就是将问题的状态进行改变。算子就是改变问题状态的操作）
      1. 分为两大类（转换和行动）
      2. 转换算子：将一个旧的RDD包装为新的RDD。可根据参数类型分为：value类型，double Value类型，key-value类型。**默认窄依赖，宽依赖标注。**
         1. value类型
            1. **map**(转换函数=>Int)
               1. 使用转换函数将RDD中所有的元素进行转换。
            2. **mapPartitions**(转换函数=>Iter)
               1. 以分区为单位进行map。获取Iter。注意**需要返回Iter。**但不要求迭代器的数量保持一致。
               2. **注意：容易内存溢出**
                  1. 会将分区的数据加载再内存中进行引用。Task没执行完时，处理完的数据不会被释放掉，会在内存中，因为存在对象的引用。所以当数据量很大的时候容易溢出。会长时间占用内存。
                  2. 当数据量大时，建议使用map
            3. **mapValues**(f)
               1. 只对每个值的values做map。
            4. **mapPartitionsWithIndex**((index, Iter)=> Iter)
               1. 获取分区和对应下标。 
            5. **flatMap**(f:T=>TraversableOnce[U]): RDD[U]  扁平化操作。
               1. 将数据map后转为一个集合。Map函数中传入为元素，传出为数组，一个元素对应一个数组。将处理的数据进行扁平化后再进行映射处理。所以算子也称作为扁平映射
               2. flatMap就是先按照传入的函数对每个元素进行map，然后再将map后的元素一起扁平化。
                  1. flatMap 的传入是一个函数对象。参数是集和的元素。返回值是一个可迭代的集和。
               3. 样例：[[1,2],[3,4]]=>[1,2,3,4]。flatmap接收的参数是数组，flat将多个数组所有元素聚合。
               4. 只有flatmap，没有flat
               5. 是一个窄依赖。就是当前分区内的数据进行操作。
            6. **glom()** 无参数=> RDD[Array[T]]   逆扁平化操作。
               1. 将一个分区所有数据转为一个集合。将同一个分区的数据转换为相同类型的内存数组进行处理。分区不变。可以理解为flat的反面。将一个分区组成一个数组返回。
               2. 样例：[1,2,3,4] 两个分区 => [[1,2],[3,4]] 将同一个分区的内容聚集在一起。
            7. **groupBy**[K](f:T=>K) => RDD[(K, Iterable[T])]  **宽依赖**
               1. 根据f返回的key进行分组。这个操作会对数据shuffle。
               2. 将数组根据制定规则进行分组。分区默认不变，但是数据会被打乱重新组合。这样的操作称作shuffle。极限情况下，数据可能被分为同一个分区中。一个组的数据在一个分区中，并不是一个分区只有一个组。
               3. **分组和分区没有必然逻辑**
            8. **filter**(f:T=>Boolean):RDD[T]
               1. 将数据根据f进行筛选，符合规则的留下。区内filter
               2. 筛选过后，分区不变。可能会出现**数据倾斜。**
            9. **sample**(withReplacement:Boolean, fraction:Double, seed:Long=Utils.random.nextLong)=>RDD[T]
               1. 抽样选取部分样本
               2. withReplacement是否放回。fraction选取每一个数的概率为多少，不放回时，fraction最高1。有放回fraction大于1时，则是每个值可能被抽到的次数。seed种子。抽取数据特殊场合有用。
               3. 不放回：伯努利算法
               4. 有放回：泊松算法
            10. **distinct(Option[numPartitions:Int]):=>RDD[T]**
               5. 根据传入的参数去重。numPartitions分区数量
               6. 底层实现时，需要考虑数据所在的分区，根据分区去重。
            11. **coalesce**(numPartitions:Int, shuffle:Boolean=false, partitionCoalescer:Option[PartitionCoalescer]=Option.empty)=>RDD[T]  **宽依赖**
                1. 缩减分区，用于大数据过滤后，提高小数据集的执行效率。使用这个函数减少分区个数。numPartitions 分区数量。
                2. 默认不会将分区的数据打乱重新组合。一个分区的数据会整个加入另一个分区。这种情况下的缩减分区会导致数据不均衡。
                3. 如果想要数据均衡。可以设置shuffle为True。但是会打乱分区。
            12. **repartition**(numPartitions:Int) **宽依赖**
                1. 扩大分区。底层调用coalesce，默认shuffle为true。
            13. **sortBy**[K](f:(T)=>K, ascending=True) **宽依赖**
                1. 根据key进行排序。但默认不改变分区，但存在shuffle操作。ascending为升序。
         2. doubule-value类型。双值函数。两个RDD。以下都是shuffle
            1. 交集 **intersection**
               1. 用法 rdd1.intersection(rdd2)。
               2. 要求两个数据源数据类型保持一致。
            2. 差集 **subtract**
            3. 并集 **union**
               1. 并集会将两个rdd合成一起。不会去重交集后合并。
               2. 示例:[[1,2]].union([[3,4]])=>[[1,2],[3,4]]
            4. 拉链 **zip**
               1. 将对应位置对应值打包成tuple。
               2. 数据源要求**分区数量**，**分组中元素的数量**保持一致。
         3. key-value类型。要求RDD是键值类型的PairRDD：RDD[K, V]。RDD[(K, V)]会隐式转换为PairRDD[K, V]。**以下的操作大部分按照Key进行**
            1. **partitionBy**(partitioner:Partitioner):RDD[(K, V)]
               1. 将数据按照传入的Partitioner重新进行分区。
               2. Spark有一个默认分区器为HashPartitioner(numPartition=n)获取分区数量和数据对应分区。
            2. **reduceByKey**(f:(V,V)=>V, Option[numPartitions]):RDD[(K, V)]  **宽依赖**
               1. 将相同的数据按照相同的key对value进行聚合。然后根据f对value依次操作。
               2. 当一个key只有一个元素时，不会参与训练。
            3. **groupByKey**(Option[numPartitions], Option[[partitioner])=>RDD[(K, Iterable[V])]   **宽依赖**
               1. 根据key 组合数据的value为List。注意没有f。
               2. 和groupBy的区别就是groupByKey会将value组合在一起。和前一个不会。
               3. 和reduceBy的对比见下面。落盘前预聚合。
            4. **aggregateByKey**(zeroValu e:U)(seqOp:(U, V)) => U, combOp(U, U)=> U):RDD[(K, U)]
               1. 将数据根据不同的规则进行分区内计算和分区间计算。传参是两个函数。一共两个要传两个参数列表
                  1. 第一个参数(括号)为初始值。制定分区内计算时，碰到的第一个值和初始值如何操作。就是分区内reduce的初始值。
                  2. 第二个参数(括号)为函数列表。第一个函数区间内计算，对象是分区内每个元素，第二个函数分区间计算，对象是每个分区提取到的每个元素。
                  3. 注意每个函数的参数类型，初始值参数类型为U。最终返回类型和初始值保持一致。
            5. **foldByKey**(zeroValue:U)(combOp(U, U)=> U):RDD[(K, U)]
               1. aggregateByKey的简化版本。当分区内和分区间操作相同的时候，只用一个函数就可以了。
            6. **combineByKey**[C]( createCombiner: V => C, mergeValue: (C, V) => C,mergeCombiners: (C, C) => C): RDD[(K, C)]
               1. 三个参数
               2. 第一个参数：将相同的第一个数据进行结构转换。实现操作。
               3. 第二个参数：分区内的计算规则
               4. 第三个参数：分区间的计算规则
            7. **join**[W](other: RDD[(K, W)]):RDD[(K, (V, W))]
               1. 在类型(K, V)和(K, W)的RDD上调用，返回一个相同key对应的所有元素连接在一起的(K, (V, W))的RDD。**类似于内连接。**
               2. 如果两个rdd中的key没有匹配上，则数据**不会**出现在结果中。
               3. 如果一个源中存在多个相同key，则另一个源会和这个源的每个相同key连接。类似笛卡尔积。
               4. 使用 rdd1.join(rdd2)。数据经过join会几何增长。会影响shuffle的性能。不推荐使用。
            8. **leftOuterJoin**[W](other: RDD[(K, W)]): RDD[(K, (V, Option[W]))]
               1. 左外连接。在右表中不存在的key会用None显示。
            9. **rightOuterJoin**
               1. 右外连接。在左表中不存在的key会用None显示。
            10. **cogroup**[W](other: RDD[(K, W)]): RDD[(K, (Iterable[V], Iterable[W]))]
                1. 和**外连接**类似。但会先在RDD内聚合后再进行外连接。先group再外连接。等于connect+group.
                2. 样例：[("a",1),("b",1)][("a",1),("a", 2)] = >[("a", (1), (1,2)), ("b", (1),())]。就是RDD内先按照key聚合，聚合的值放在一起。然后rdd间按照key进行外连接。没有的值为空。
      3. 行动算子：出发任务的调度和作业的执行。
         1. 解释。行动算子会触发作业的执行。底层调用的是sc.runJob方法。创建ActiveJob 并执行
         2. **reduce**(f: (T, T) => T): T
            1. 聚合元素并输出。
         3.  **collect**(): Array[T]
            2. collect收集所有的数据并打印。
         4. **count**(): Long
            1. 返回数据源中的个数。
         5. **first**()T:
            1. 返回第一个
         6. **take**(num: Int): Array[T]：
            1. 获取num个数据
         7. **takeOrdered**(num: Int)(implicit ord: Ordering[T]): Array[T]
            1. 将RDD排序后返回前n个元素。默认升序。
            2. 降序takeOrdered(n)(降序)
         8. **aggregate**[U: ClassTag](zeroValue: U)(seqOp: (U, T) => U, combOp: (U, U) => U): U
            1. 初始值、分区内、分区间的计算规则。
            2. 会直接返回结果。不需要考虑键值类型，普通类型就能用。
            3. 和aggergateByKey的不同
               1. aggergateByKey仅参与分区内的运算
               2. aggregate会参与分区内和分区间的运算。
         9. **fold**(zeroValue: T)(op: (T, T) => T): T
            1.  分区内、分区间的规则相同时，使用fold。其他没有不同
         10. **countByKey**(): Map[K, Long]
             1. 统计key-value RDD中key出现的次数
         11. **countByValue**():
             1. 获取每个value和其对应的出现次数
         12. foreach
             1. executor端对分区里的数据执行foreach。不是按照executor顺序打印。
             2. collect后foreach是先收集数据并返回到driver，按照分区顺序采集executor并打印。
             3. 由于RDD需要发送到executor端。所以foreach中用到的对象都需要序列化。样例类可以自动序列化。
             4. RDD算子传递的函数是会包含闭包操作，就会进行检测功能。会检测是否能序列化。
             5. 这个不太懂，算了。
   5. 分区器：
      1. 分区器有两个需要实现的。numPartitions, getPartition
      2. numPartitions为分区数量。
      3. getPartition根据Key获取该Key所在的分区。
      4. 分区器有HashPartitioner, RangePartitioner, PythonPartitioner.
4. RDD序列化
   1. **算子以外的代码都是在Driver 端执行, 算子里面的代码都是在 Executor 端执行**。那么在 scala 的函数式编程中，就会导致**算子内经常会用到算子外的数据**，这样就 形成了闭包的效果，如果使用的算子外的数据**无法序列化**，就意味着无法传值给 Executor 端执行，就会发生错误，所以需要在执行任务计算前，检测**闭包内的对象**是否可以进行序列化，这个操作我们称之为**闭包检测**。即检测RDD操作内部（RDD函数执行的操作）是否使用的都是能序列化的值。
      1. rdd.filter(this.query) 这个时候因为使用了this,所以会检测this所代表的对象能否序列化
      2. scala中类的构造参数是类的属性。构造参数需要进行闭包检测.类也需要进行闭包检测
   2. 可以使用kryo序列化操作来序列化，减少字节传输量。
5. RDD依赖关系
   1. 直接依赖关系称为依赖。间接依赖关系为血缘关系
   2. 每个RDD保存血缘关系。当某一个RDD出现运算错误的时候，该RDD可以通过血缘关系从数据源重新获取数据。
   3. rdd.dependencies 打印依赖关系
      1. 新RDD依赖于旧RDD。当不存在shuffle时，是窄依赖（一对一）依赖，指分区一对一的依赖。（OneToOneDependency)
      2. 当存在shuffle的时候，是宽依赖。叫shuffle依赖。(ShuffleDependency)
   4. rdd.toDebugString ：打印血缘关系。没有括号注意。
      1. 当**存在shuffle操作**的时候，血缘关系会产生**缩进**的效果
      2. (2) ShuffledRDD[2] at reduceByKey at <console>:25 []
         1. +-(2) MapPartitionsRDD[1] at map at <console>:25 []
         2.    |  ParallelCollectionRDD[0] at makeRDD at <console>:25 []
         3. 其中(2)表示的是分区数量。+-表示shuffle操作。
   5. 一个分区的多个连续窄依赖会集成成一个Task后再执行。宽依赖会等多个分区的窄依赖Task运行结束后执行。上述两个操作是分阶段进行的。先进行窄依赖Task阶段。再进行宽依赖Task阶段。
   6. 阶段：根据DAG（Directed Acyclic Graph)有向无环图组成拓扑图，构建转换过程和任务阶段。shuffle操作产生一个新阶段。
   7. RDD的阶段划分：
      1. 每存在一个shuffleRDD时，阶段会自动增加一个。阶段数量=shuffle依赖的数量+1.ResultStage只会出现一次，在最后一次执行。
   8. RDD的任务划分：
      1. RDD任务切分中间分为：Application、Job、Stage 和 Task 
      2. ⚫ Application：初始化一个 SparkContext 即生成一个Application； 
      3. ⚫ Job：一个**Action 算子**行动算子就会生成一个 Job； 
      4. ⚫ Stage：Stage 等于宽依赖(ShuffleDependency)的个数加 1；
      5. ⚫ Task：一个**Stage 阶段**中，**最后一个RDD的分区**个数就是 Task 的个数。
      6. 注意：Application->Job->Stage->Task 每一层都是 1 对 n 的关系。
      7. 阶段名称和任务名称相同，如ShuffleMaskStage对应任务ShuffleMaskTask
6. RDD持久化
   1. 如果多个行动算子存在相同的前部分操作，则RDD对象可以重用。但由于RDD中不存储数据，所以数据无法重用，每个行动算子会从头获取数据并计算。
   2. 如果为了性能需要重用中间数据，我们应该**持久化存储**中间存储。可以存在内存中（速度快不安全）或者磁盘中（慢但安全）。
      1. rdd.persist()则这个rdd会持久化存储。后面重用这个rdd对象的时候，会从cache中读取数据，而不是重复计算。默认保存到内存中，如果需要保存到磁盘中，需要传入参数StorageLevel.***
         1. ***可以为：DISK_ONLY, MEMORY_ONLY, MEMORY_AND_DISK等等。
         2. persist会在血缘关系中添加新的依赖。如果出现问题，可以重头读取数据。cache一样。
      2. 代码rdd.cache() 调用了persist()。将数据保存在内存中。
         1. 注意cache持久化操作，会在行动算子执行时才触发。
         2. cache会保存在临时文件夹下。作业结束后，会被删除。
      3. rdd.checkpoint() 检查点操作。会将算子落盘。一般保存hdfs中。且checkpoint操作会独立执行作业。
         1. sc.setCheckpointDir("cp")设置检查点目录。
         2. checkpoint执行过程中，由于从磁盘中读取数据，会切断血缘关系，重新建立从磁盘中读取数据的血缘关系。等同于改变数据源。
   3. 持久化区别
      1. cache: 将数据临时存储在内存中进行数据重用。
      2. persist：将数据临时存在磁盘中进行重用。涉及IO性能较低。作业执行完毕。临时存储的文件就会丢失。
      3. checkpoint：将数据长久的保存在磁盘中。性能较低。为了保证数据安全。一般情况下，会独立执行一个作业（额外的作业），产生数据文件来长期存储。一般情况和cache联合使用。
         1. 解释：checkpoint()调用的时候，会触发作业执行操作。相当于一个行动算子。如果在这之前调用了cache()，则会从cache中取出数据，而避免重复运算。
   4. 持久化操作的应用：
      1. rdd被多个行动算子重复使用。
      2. 单个rdd走的路程太长，为了避免出错，或者数据比较重要的场合。可以持久化中间步骤。
7. RDD分区器。
   1. 分区相关API：
      1. partitionBy，根据传入的自定义分区器进行分区。coalesce重新设置数据分区。repartition同coalesce。
   2. 自定义分区器。
      1. 继承类： extends Partitioner{}
      2. 重写两个方法：
         1. override def numPartitions: Int。 分区数
         2. override def getPartition(key:Any): Int=??? 根据数据的key返回数据所在的分区索引（从0开始）。
   3. Spark 目前支持**Hash 分区**和**Range 分区**，和用户自定义分区。Hash 分区为当前的默认 分区。分区器直接决定了RDD中分区的个数、RDD中每条数据经过 Shuffle 后进入哪个分区，进而决定了Reduce 的个数。
      1. 只有Key-Value 类型的RDD才有分区器，非Key-Value 类型的RDD分区的值是None
      2. 每个RDD的分区 ID 范围：0 ~ (numPartitions - 1)，决定这个值是属于那个分区的
   4. **Hash 分区**：对于给定的 key，计算其 hashCode,并除以分区个数取余
   5. **Range 分区**：将一定范围内的数据映射到一个分区中，尽量保证每个分区数据均匀，而 且分区间有序
8. RDD文件读取和保存：
   1. Spark 的数据读取及数据保存可以从两个维度来作区分：**文件格式**以及**文件系统**。 文件格式分为：text 文件、csv 文件、sequence 文件以及Object 文件；文件系统分为：本地文件系统、HDFS、HBASE 以及数据库。
   2. 存储：
      1. RDD.saveAsTextFile(path)
      2. RDD.saveAsObjectFile(path)
      3. RDD.saveAsSequenceFile(path) 要求必须是key-value RDD
   3. 读取
      1. sc.textFile("output")
      2. sc.sequenceFile[Int,Int]("output")
      3. sc.objectFile[Int]("output"
9. 三大数据结构：
   1. RDD：弹性分布式数据集
   2. 累加器：分布式共享只写变量
   3. 广播变量：分布式共享只读变量
10. 累加器
    1. 为什么需要累加器？
        1. spark分布式框架，相当于一个多线程的task。而且是发送到执行端executor执行。而且executor执行的task没有返回操作。无法修改同时修改本地的数据。累加器的作用就是在task执行完毕后，从task返回到driver端。
        2. 累加器用来把 Executor 端变量信息聚合到Driver 端。在Driver 程序中定义的变量，在 Executor 端的**每个 Task**都会得到这个变量的一份新的副本，每个 task 更新这些副本的值后，**传回Driver 端进行merge**。
    2. 使用
       1. sc.longAccumulator(name="sum")
          1. 整型累加器。
          2. ac.add
          3. ac.value
       2. sc.doubleAccumulator
       3. sc.collectionAccumulator
          1. List类型的累加器。
    3. 自定义累加器：
       1. 继承： extends AccumulatorV2[In, Out]
          1. 定义泛型In :累加器输入的数据类型 Out: 累加器返回的数据类型。
             1. 如: extends AccumulatorV2[String, mutable.Map[String, Long]]
          2. 重写方法：
             1. isZero: Boolean  判断是否是初始状态。
             2. add(In): 获取累加器需要计算的值
             3. copy(): 复制一个新的累加器
             4. reset(): 重置累加器
             5. merge(): 合并多个累加器
             6. value(): Out 返回累加器的结果
       2. 使用步骤：
          1. 创建累加器对象
          2. 向spark注册。sc.register(累加器，name="xx")
    4. 累加器的问题：
       1. 少加。如果转换算子中调用累加器。如果没有行动算子，那么不会执行。
       2. 多加。如果多次调用行动算子，则会多次执行，导致多次累加。
          1. 所以一般情况下，累加器会在行动算子中进行操作。即写在行动算子中。
       3. 多个Task的累加器是不能相互访问的。
11. 广播变量
    1. **广播变量用来高效分发较大的对象。**向所有工作节点发送一个较大的只读值，以供一个 或多个 Spark 操作使用。比如，如果你的应用需要向所有节点发送一个较大的只读查询表， 广播变量用起来都很顺手。**在多个并行操作中使用同一个变量，但是 Spark 会为每个任务分别发送**。
    2. 闭包数据，都是以task为单位发送的，每个任务中包含闭包数据，这样可能导致一个executor中含有大量重复的数据，并且占用大量的内存。Executor就是一个JVM，启动时会分配内存。完全可以将闭包数据放在executor中，达到共享的目的。这些放在内存的数据称为广播变量。广播变量不能被更改。分布式的只读变量。
    3. 使用：
       1. 初始化bc = sc.boardcast(variable)
       2. 方位bc.value 就是variable




# spark性能优化相关名词解释
1. shuffle
   1. 不同分区内的数据需要聚合。这种操作即宽依赖操作。即是shuffle操作。
   2. 针对同一个数据的多次shuffle，spark会在底层优化缓存。
2. 落盘
   1. 当涉及shuffle操作的时候，即宽依赖的时候，不能在内存中存储数据，会容易溢出。必须**落盘**处理。即将符合条件的数据存储到一个文件中。再从文件中读取。所以shuffle的性能非常低。
3. 预聚合功能
   1. 在落盘之前，在分区内预聚合。有效的而减少shuffle时落盘的数据量。


# 架构
Java的架构：
MVC: Model View Controller 架构。
Model，模型：业务模型和数据模型（封装）。
View视图是数据展示
Controller是控制层。控制数据的流转

大数据中一般不需要View。所以不用MVC模式。改用三层架构：
Controller(控制层), service(服务层), dao(持久层)。
Application=》controller进行调度=》service(启动服务)=>dao(持久层)访问数据。
common 一些共同的代码放在这。
util 一些工具类放在这。哪里都能用的工具。
bean 实体类
application 应用类
controller 控制类
service 服务类
dao 持久层，操作数据。


问题：
1. reduceByKey和groupByKey的区别
   1. 性能上：
      1. reduceByKey会在区内进行聚合，然后再落盘。所以数据量会小很多。比groupByKey快很多，性能更高。就是所谓的预聚合功能
   2. 功能上：
      1. groupByKey只分组，不聚合。reduceByKey分组且聚合。
2. reduceByKey, aggregateByKey, foldByKey, combineByKey底层调用都是combineByKeyWithTags(createCombiner, mergeValue, mergeCombines).设定初始值，然后分区内聚合，然后分区间聚合。


题目：（做过的题目都得记录，不然很容易忘）
1. 创建数据
   1. sc.makeRDD(List(1,2,3,4), numSlices=2)
2. 分区内最大值，分区间最大值求和。
   1. 使用mapPartitions求出分区最大值，然后collect。
      1. rdd.mapPartitions(list=>Iterator(list.max)).collect().sum
      2. 这里的list是val的名称。Iterator是获得一个Iterator对象。
   2. 使用glom求出分区，然后map取最大值，然后collect求和。
      1. rdd.glom().map(_.max).collect()
   3. 当使用key、value组成对时即List(("a", 1), ("a", 2), ("a", 3), ("a", 4))这样子。可用aggregateByKey
      1. rdd.aggregateByKey(0).(math.max(_,_), _+_).collect()
3. wordCount
   1. 数据 sc.makeRDD(List("Hello spark", "Hello scala"), numSlices=2).flatMap(_.split(" "))
   2. 方法：
      1. 使用groupBy 转换为iter后统计数量
         1. rdd.groupBy(word=>word).mapValues(iter=>iter.size)
      2. 使用map转为key, value RDD，使用reduceByKey, aggregateByKey, foldByKey中的一个
         1. rdd.map((_, 1)).foldByKey(0)(_+_).collect()
      3. 双值countByKey
      4. countValue单值。
      5. 累加器实现。
4. 相同Key的平均值
   1. 数据List(("a", 1), ("b", 3),("b", 4), ("a", 3), ("a", 3),("b", 4))
   2. 统计Key的总和和出现的次数
      1. rdd.aggregrateByKey((0,0))((t, v)=>(t._1+v, t._2+1), (t1, t2)=>(t1._1+t2._1, t1._2+t2._2)).map(a=>a._1, a._2._1/a._2._2)
      2. rdd.combineByKey(v=>(v,1), (t:(Int, Int), n:Int)=>(t._1+n, t._2+1), (t1:(Int, Int), t2:(Int, Int))=>(t1._1+t2._1, t1._2+t2._2))
         1. 这个操作是对相同key的value做聚合。所以key是不会传进来的。
         2. 这里需要注意Scala的语法。由于tuple是中途产生的，所以scala并不理解t的类型是什么。scala是静态语言，这样没法编译。所以我们需要标注类型，才能让它正常的编译。
5. 统计每一个省份每个广告被点击数量排行的Top3
   1. 数据： xxxx 河北  北京  张三 广告A
   2. 思路，首先仅提取需要的特征 河北、广告A。思路按照省分类统计广告的点击次数，然后再按照省份进行归纳。你的思路是首先按照省分类，再统计广告次数。为什么这么做不好？不好写
   3. 首先用map创造数据，使用split分割。分割后的数据 List((省份,广告),1)
   4. 然后按照 省份-广告 作为key 进行聚合
   5. 再根据 省份 作为key 进行聚合。

   rdd.map(data=>{val datas=data.split(" ");((datas(1), datas(4)),1)})

   rdd.reduceByKey(_+_)

   rdd.map{case ((prv, ad), sum) =>{(prv, (ad, sum))}}

   rdd.groupByKey().mapValues(iter=>iter.toList.sortBy(_._2)(Ordering.Int.reverse).take(3))
6. top10热门种类。
   1. 需求：按照点击数排名。靠前的就排名高。再比较点击数、下单数、支付数。
   2. 实现一：
      1. 首先filter出点击数量等分类存在的值=》进行map为(种类，1)=>reduceByKey。统计每个种类的个数=>三个种类进行连接。(种类ID，(点击数量)，(下单数量),(支付数量))
      2. 这里有多种连接方式：join,zip, leftOuterJoin, cogroup. join不行，因为可能存在三个种类一个不存在。leftOuterJoin不行，同样必须外连接。zip不行，zip连接不会按照key连接，而是按照分区内数据的数量和位置连接。cogroup是外连接。所以可行: a.cogroup(b,c)
      3. 连接起来后，将同id的几个种类值相加 a.mapValues()
      4. 进行排序a.sortBy(_._2, ascending=false).take(10)。按照第二个就是元组进行排序。先排元组第一个值，再排第二个值。
   3. 优化一：
      1. 多个种类调用读取数据textFile。所以cache这个RDD。
      2. cogroup是shuffle操作，性能较低。
         1. map数据 => (品类ID，(点击数量,0,0))。**将所有数据转换为相同格式后相加。**
         2. 然后a.union(b).union(c)
      3. 再排序等等。
   4. 优化二：
      1. 存在大量的reduceByKey操作。
      2. 将数据转换结构：（品类ID，（1，0，0）），（品类ID，（0，1，0））
      3. 完整代码：

```scala
val flatRDD=actionRDD.flatMap(
   action=>{
      val datas=action.split("_"); 
      if(datas(6)!="-1")
      {List((datas(6),(1,0,0)))}
      else if (datas(8)!="null")
      {datas(8).split(",").map(id=>(id, (0,1,0)))}
      else if(datas(10)!="null"){datas(10).split(",").map(id=>(id,(0,0,1)))}
      else{Nil}})
flatRDD.reduceByKey((t1,t2)=>(t1._1+t2._1,t1._2+t2._2,t1._3+t2._3)).sortBy(_._2,false).take(10)
```
   5. 优化三：
      1. 不用shuffle操作。使用累加器。
```scala
case class HotCategory(cid:String, clickCnt:Int, OrderCnt:Int, payCnt:Int)

class HotCategoryAccumulator extends AccumulatorV2[(String,String),mutable.Map[String,HotCategory]]{
   // IN:(品类ID，行为类型)
   // out: mutable.Map[String, HotCategory]
}

```

7. top10品类中，sessionID top10统计。
   1. 需求分析：top10热门品类中，每个品类点击Top10的session。可以先统计出top10的热门品类。然后统计session。将项目映射为 (品类id, session, 1)。然后按照品类、session进行相加。再按照品类id进行聚合起来。然后再进行排序取前10个。思路和各省份广告点击前10相同。
   2. 首先map((省份，广告)，1)。然后按照省份广告相加。然后按照省份进行聚合。然后按照次数进行排序。
8. 页面单跳转换率统计。 
   1. 需求分析：数据： session id， 访问页面， 时间。
   2. 目标是求 A->B 的次数/ A的次数。所以首先统计A的次数。直接wordcount。然后统计A->B的次数。按照session id分组groupBy，然后按照时间排列。然后拉链 形成 A->B。然后再wordCount.
   3. 优化:
      1. 不用统计所有页面。只用统计部分页面。所以我们对部分页面过滤一下就行。